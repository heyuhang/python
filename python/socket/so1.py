# coding: utf-8
import socket

host = '127.0.0.1'
port = 5678

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#TCP
s.bind((host, port))
#bind socket
s.listen(1)
#listen connection

while 1:
	#while loop, set program response many client
	clientSocket, clientAddr = s.accept()
	#accept client connection
	print 'Client connected!'
	clientSocket.sendall('Welcome to Python World!')
	#send string to client
	clientSocket.close()
	#close connection

