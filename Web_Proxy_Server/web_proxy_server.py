#this is my Web proxy server
#tju scs 3013218065 wwx
#in this project,I use the socket to get the information 
#and use the info to change the get and connect the new URL
#and recv the info form this page and pass the info to the clicker
import socket
import string
import re
#this is my localhost server
seraddr=('127.0.0.1',8081)
#this is default socket
apaaddr=('e.tju.edu.cn',80)
#use the TCP
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#the server bing the URL and socket
ser.bind(seraddr)
ser.listen(5)
poll=[]
# use this to always listen and work
while True:
	#get the info
	con,addr=ser.accept()
	poll.append(con)
	#use the info to enter the webpage and get it
	while len(poll):
		#the new socket to enter the new webpage
		apaser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		c=poll.pop(0)
		#receive the info ,you want
		buf=c.recv(1024000000)
		#we can see the info you send to Web proxy server
		print buf
		try:
			hehe1 = buf.split(' ')[0]
			#get the URL
			src2 = buf.split(' ')[1]
			src1 = src2[1:]
			print src1
		except:
			continue
		#we get the new socket and look the info
		apaaddr=(src1,80)
		buf = re.sub(src2,'/',buf)
		print buf
		print type(buf),type('yoyoy')
		if not buf:
			continue
		print apaaddr
		apaser.connect(apaaddr)
		apaser.send(buf)
		#get the info
		data=apaser.recv(10240000)
		#send the info to your browser
		print data
		c.send(data)
		apaser.close()
ser.close()