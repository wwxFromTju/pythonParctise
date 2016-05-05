import argparse
import httplib
import urlparse
import re
import urllib
DEFAULT_URL = 'http://e.tju.edu.cn'
HTTP_GOOD_CODES = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]

def get_server_status_code(url):
	host,path = urlparse.urlparse(url)[1:3]
	try:
		#conn = httplib.HTTPConnection(host)
		conn = httplib.HTTPConnection(url)
		conn.request('HEAD', path)
		return conn.getresponse().status
	except StandardError:
		return None
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "hehe")
	parser.add_argument('--url', action="store", dest="url", default=DEFAULT_URL)
	given_args = parser.parse_args()
	url = given_args.url
	if get_server_status_code(url) in HTTP_GOOD_CODES:
		print "%s is ok" %url
	else:
		print "%s err"%url