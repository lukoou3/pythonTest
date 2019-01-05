from socket import *
mSocket = socket(AF_INET,SOCK_DGRAM)
mSocket.sendto("你好啊hahahaha".encode("utf-8"),("192.168.0.100",9502))