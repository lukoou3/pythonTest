from scapy.all import *

ap_list = []

p = None
def PacketHandler(pkt):
    global p
    p = pkt
    print(pkt)
    if pkt.haslayer(Dot11):

        if pkt.type == 0 and pkt.subtype == 8:

            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)

                print
                "AP MAC: %s with SSID: %s " % (pkt.addr2, pkt.info)


sniff(filter="udp and (port 9503)",prn=PacketHandler,count=1)

"""
https://www.cnblogs.com/xuanhun/p/5625186.html
http://www.cnblogs.com/jingmu/articles/7424787.html
"""