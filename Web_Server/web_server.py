#this is Web server
#tju scs 3013218065 wwx
#in this project i creat the Web server to deal the GET and HEAD
#i use the RequestHandler to overwrite the GET method and HEAD method
#do_GET methon is my browser to ask to GET than my code will call it
#do_HEAD methon is my browser to ask to HEAD than my code will call it 
import argparse
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#this this my localhost and port 
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8800

#use this class to overwrite thr GET
#i call do something when you use the GET to my Web server
class RequestHandle(BaseHTTPRequestHandler):
	"""docstring for RequestHandle"""	
	def do_GET(self):
		#this is head
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		#this is body ,you can see it in the browser
		self.wfile.write(" ask your GET method -------from: wwx ")
		return
	def  do_HEAD(self):
		#this is head in the browser
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		return

	

#use this class to Inheritance the HTTPServer class
#and set the port and host 
#and if you connect the server, than The Web Server will call 
#the RequestHandle class to deal the GET
class CustomHTTPServer(HTTPServer):
	"""docstring for CustomHTTPServer"""
	def __init__(self, host, port):
		server_address = (host, port)
		HTTPServer.__init__(self, server_address, RequestHandle)


#use this method to start my Web server and listen the request
def run_server(port):
	try:
		server = CustomHTTPServer(DEFAULT_HOST, port)
		print "CustomHTTPServer %s" % port
		server.serve_forever()
	except Exception,  err:
		print "Error: %s" %err
	except KeyboardInterrput:
		server.socket.close()


#this is you start the code ,this code will call
parser = argparse.ArgumentParser(description='Simple HTTP Server')
parser.add_argument('--port', action = "store", dest="port", type = int, default = DEFAULT_PORT)
given_args = parser.parse_args()
port = given_args.port
run_server(port)
