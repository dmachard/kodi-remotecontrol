
import socket
import time
import struct

PT_ACTION = 0x0A

ACTION_EXECBUILTIN = b"\1"

class EventClient:
    def __init__(self, api_host,
                       api_port=9777):
        """authenticator class"""
        self.api_host = api_host
        self.api_port = api_port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def get_header(self, psize, ptype):
        """
        /*     -----------------------------                                    */
        /*     | -H1 Signature ("XBMC")    | - 4  x CHAR                4B      */
        /*     | -H2 Version (eg. 2.0)     | - 2  x UNSIGNED CHAR       2B      */
        /*     | -H3 PacketType            | - 1  x UNSIGNED SHORT      2B      */
        /*     | -H4 Sequence number       | - 1  x UNSIGNED LONG       4B      */
        /*     | -H5 No. of packets in msg | - 1  x UNSIGNED LONG       4B      */
        /*     | -H6 Payload size          | - 1  x UNSIGNED SHORT      2B      */
        /*     | -H7 Client's unique token | - 1  x UNSIGNED LONG       4B      */
        /*     | -H8 Reserved              | - 10 x UNSIGNED CHAR      10B      */
        /*     |---------------------------|                                    */
        /*     | -P1 payload               | -                                  */
        /*     -----------------------------                                    */

        uint16 = !H
        uiint32 = !I
        """
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
        """connect to event servers"""
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