import sys
import struct
from scapy.all import *

data = struct.pack('=BHI', 0x12, 20, 1000)
pkt = IP(src='192.168.0.101', dst='192.168.0.100')/UDP(sport=12345,dport=9502)/data
send(pkt, inter=1, count=5)