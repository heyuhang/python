#coding: utf-8
import socket
#conect port 5678 and read socket print result on screen

host = '127.0.0.1'
port = 5678
#udp: socket.SOCK_DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while 1:
	buf = s.recv(2048)
	if not len(buf):
		break
	print buf
