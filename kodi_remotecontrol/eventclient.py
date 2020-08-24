
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
                       api_http_port=8080,
                       api_http_login=None,
                       api_http_pwd=None):
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
                    logging.debug("Pinging backend...")
                    r = requests.post(url=api_url, json=p)
                    
                    if r.status_code == 200:
                        logging.debug("Backend response: %s" % r.json()['result'])
                    elif r.status_code == 401:
                        logging.debug("Got an unauthorized response, make sure you don't have a password for the Web Server")
                    else:
                        logging.debug("Got code: %i from backend, continuing..." % r.status_code)
                    
                    kodi_ready = True
                except requests.exceptions.ConnectionError:
                    logging.debug("Failed to ping backend, make sure that Kodi is running. Retrying in 10 sec")
                    time.sleep(10)

        if timeout_raised:
            raise Exception( "Kodi is not running?" )

        if kodi_ready:
            logging.debug("Event UDP channel initialization...")
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

    def press_reset(self):
        """refresh token"""
        logging.debug("Refresh udp connection")
        self.api_token = int(time.time())
        self.send_helo()

    def press_play(self):
        """press play button"""
        self.send_action(msg="Action(Play)")

    def press_pause(self):
        """press pause button"""
        self.send_action(msg="Action(Pause)") 

    def press_stop(self):
        """press stop button"""
        self.send_action(msg="Action(Stop)") 

    def press_osd(self):
        """press osd button"""
        self.send_action(msg="Action(OSD)") 

    def press_playlist(self):
        """press playlist button"""
        self.send_action(msg="Action(Playlist)")

    def press_next(self):
        """press next button"""
        self.send_action(msg="Action(SkipNext)") 

    def press_previous(self):
        """press previous button"""
        self.send_action(msg="Action(SkipPrevious)") 

    def press_left(self):
        """press left button"""
        self.send_action(msg="Action(Left)") 

    def press_right(self):
        """press right button"""
        self.send_action(msg="Action(Right)") 

    def press_up(self):
        """press up button"""
        self.send_action(msg="Action(Up)")  

    def press_down(self):
        """press down button"""
        self.send_action(msg="Action(Down)")  

    def press_enter(self):
        """press enter button"""
        self.send_action(msg="Action(Select)")  

    def press_back(self):
        """press back button"""
        self.send_action(msg="Action(Back)")  

    def press_ctxmenu(self):
        """press contextual menu button"""
        self.send_action(msg="Action(ContextMenu)")  

    def press_logoff(self):
        """press logoff button"""
        self.send_action(msg="System.LogOff")  

    def press_subtitle(self):
        """press subtitle button"""
        self.send_action(msg="Action(NextSubtitle)")  

    def press_language(self):
        """press language button"""
        self.send_action(msg="Action(AudioNextLanguage)")  