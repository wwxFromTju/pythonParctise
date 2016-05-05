from socket import *
import time
HOST='127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
	time.sleep(1)
	udpCliSock.sendto(" ",ADDR)
	data1,ADDR = udpCliSock.recvfrom(BUFSIZ)
	print data1
	 