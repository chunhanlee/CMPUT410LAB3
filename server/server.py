#!/usr/bin/env python
# code borrowed from https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8888)
handler.cgi_directories = ["/cgi"]
 
httpd = server(server_address, handler)
print "Starting server ..."
httpd.serve_forever()
