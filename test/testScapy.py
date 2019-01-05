import struct
from scapy.all import *

data = [0x02,0x80, 0, 0 ,0,0xcc,0x70,0x02020209,0x03,0x03,''.encode(),'bbbd'.encode()]
buffer = struct.pack("!HHIIIHHIII32s64s", *data)
pkt = IP(src='10.24.40.45', dst='10.24.41.168')/UDP(sport=12345, dport=9502)/buffer
send(pkt, inter=1, count=1)


data = [0x02,0x64,0x5bf4d554, 0x0027df6d ,0x0a18282d,0xc9,0x54]#报文头
data.append(0x04)
data.append(0x03)
data.append(0x0000)
data.append(0x04)
data.append(0x11)
data.append(0x2828001c)
data.append(0x32320002)
data.append(0x00000400)
data.append(0x00000400)
data.append(0x3000000a)
data.append(int(time.time()))#
data.append(0x0000035d)
data.append(0x00209400001b12ac)
data.append(''.encode())
buffer = struct.pack("!HHIIIHHIIHBBIIIIIIIQ32s", *data)
pkt = IP(src='10.24.40.45', dst='10.24.41.168')/UDP(sport=9501, dport=9502)/buffer
send(pkt)