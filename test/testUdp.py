from socket import *
import struct
import time

def testScan():
    data = [0x02,0x80, 0, 0 ,0,0xcc,0x70,0x02020209,0x03,0x03,''.encode(),'bbbd'.encode()]
    buffer = struct.pack("!HHIIIHHIII32s64s", *data)
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    sendAddr = ("10.24.123.105", 9502)#"192.168.37.13"
    udpSocket.sendto(buffer, sendAddr)
    udpSocket.close()

def testMomit():
    data = [0x02,0x80, 0, 0 ,0,0xc9,0x70]#报文头
    data.append(0x04)
    data.append(0x03)
    data.append(0x00)
    data.append(0x04)
    data.append(0x06)
    data.append(0x02020209)
    data.append(0x02020210)
    data.append(0xCA)
    data.append(0xCCCC)
    data.append(0x04)
    data.append(int(time.time()))
    data.append(0x14)
    data.append(0x0202020902020209)
    data.append(0x00)
    data.append(0x00)
    data.append(0x00)
    data.append(0x00)
    buffer = struct.pack("!HHIIIHH IIHBBIIIIIIIQQQQQ", *data)
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    sendAddr = ("10.24.123.105", 9502)#"192.168.37.13"
    udpSocket.sendto(buffer, sendAddr)
    udpSocket.close()

if __name__ == "__main__":
    testScan()
    testMomit()