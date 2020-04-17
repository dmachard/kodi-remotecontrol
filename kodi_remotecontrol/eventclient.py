
import socket
import time
import struct

PT_ACTION = 0x0A

ACTION_EXECBUILTIN = b"\1"

class EventClient:
    def __init__(self, api_host,
                       api_port=9777):
        """event client class"""
        self.api_host = api_host
        self.api_port = api_port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_header(self, psize, ptype):
        """return udp header packet"""
        sig = b'XBMC'
        ver = b'\2\0'
        reserved = b"\0" * 10
        uid = int(time.time())
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
        addr = (self.api_host, self.api_port)
        self.sock.sendto(pkt, addr)

    def send_action(self, msg):
        """send action packet https://kodi.wiki/view/Action_IDs"""
        pkt_action = ACTION_EXECBUILTIN + msg.encode() + b"\0"
        pkt_header = self.get_header(psize=len(pkt_action),
                                     ptype=PT_ACTION)
        pkt = pkt_header + pkt_action
        self.send_packet(pkt=pkt)

        return None