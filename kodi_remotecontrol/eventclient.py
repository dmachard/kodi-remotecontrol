
import socket
import time
import struct
import requests
import logging

PT_ACTION = 0x0A
PT_HELO = 0x01
PT_BYE = 0x02
PT_PING = 0x05

ACTION_EXECBUILTIN = b"\1"

class EventClient:
    def __init__(self, api_host,
                       api_udp_port=9777,
                       api_http_port=8080
                       ):
        """event client class"""
        self.api_host = api_host
        self.api_udp_port = api_udp_port
        self.api_http_port = api_http_port

        self.api_token = int(time.time())
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', 1444))

        self.start_client()

    def start_client(self):
        """start client only if kodi is ready"""
        logging.debug("Checking if the backend is online...")

        timeout_max = 120
        timeout_raised = False
        kodi_ready = False
        start_time = time.time()
        p = {"method": "JSONRPC.Ping", "id": 1, "jsonrpc": "2.0"}
        api_url = "http://%s:%s/jsonrpc" % (self.api_host, self.api_http_port)

        while (not kodi_ready) and (not timeout_raised):
            if (time.time() - start_time) >= timeout_max:
                timeout_raised = True
            else:
                try:
                    # send ping to kodi jsonrpc api
                    r = requests.post(url=api_url, json=p)
                    logging.debug("Backend response: %s" % r.json())
                    kodi_ready = True
                except requests.exceptions.ConnectionError:
                    pass
                    time.sleep(10)

        if timeout_raised:
            raise Exception( "Backend api not ready ?" )

        if kodi_ready:
            logging.debug("Backend is ready")
            self.send_helo()

    def refresh_connection(self):
        """refresh token"""
        logging.debug("Refresh udp connection")
        self.api_token = int(time.time())
        self.send_helo()

    def get_header(self, psize, ptype):
        """return udp header packet"""
        sig = b'XBMC'
        ver = b'\2\0'
        reserved = b"\0" * 10
        uid = self.api_token
        seq = 1
        maxseq = 1

        return sig + struct.pack('!2B H L L H L 10B',  
                                 *ver,
                                 ptype,
                                 seq,
                                 maxseq,
                                 psize,
                                 uid,
                                 *reserved)

    def send_packet(self, pkt):  
        """connect to event servers and send packet"""
        addr = (self.api_host, self.api_udp_port)
        self.sock.sendto(pkt, addr)

    def send_helo(self):
        """send helo packet"""
        logging.debug("Sending helo packet")

        device_name = b"REMOTECONTROL" + b"\0"
        icon_type = b"\0"
        port_no = 0
        reserved1 = 0
        reserved2 = 0

        pkt_helo = device_name + struct.pack('!cHII', icon_type, port_no, reserved1, reserved2)
        pkt_header = self.get_header(psize=len(pkt_helo),
                                     ptype=PT_HELO)

        pkt = pkt_header + pkt_helo
        self.send_packet(pkt=pkt)

    def send_bye(self):
        """send bye packet"""
        logging.debug("Sending bye packet")

        pkt = self.get_header(psize=0, ptype=PT_BYE)
        self.send_packet(pkt=pkt)

    def send_ping(self):
        """send ping packet"""
        logging.debug("Sending ping packet")

        pkt = self.get_header(psize=0, ptype=PT_PING)
        self.send_packet(pkt=pkt)

    def send_action(self, msg):
        """send action packet
        https://kodi.wiki/view/Action_IDs
        https://kodi.wiki/view/List_of_built-in_functions
        """
        logging.debug("Sending action packet")

        pkt_action = ACTION_EXECBUILTIN + msg.encode() + b"\0"
        pkt_header = self.get_header(psize=len(pkt_action),
                                     ptype=PT_ACTION)
        pkt = pkt_header + pkt_action
        self.send_packet(pkt=pkt)

        return None