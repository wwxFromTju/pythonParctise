#this is my UDP ping server
#tju scs 3013218065 wwx
#in this project, I use the server to listen the
#query from the click and than send the time to 
#the click

from socket import *
import time

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST, PORT)

#bind the the server to the UDP Server
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while  True:
	print 'waiting for connection...'
	#recv the data from the click
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	print '...connected from:', addr
	#send the time to the click
	ans =  time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
	udpSerSock.sendto(' %s' % ( ans),addr) 
tcpSerSock.close()