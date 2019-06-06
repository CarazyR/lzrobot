#! /usr/bin/python
# -*- coding: utf-8 -*-
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("192.168.0.108",12345)
print "Staring up on %s:%s" %  server_address
sock.bind(server_address)
sock.listen(5)
 
while True:
    print "waiting .........."
    connetion,client_address = sock.accept()
    while True:
        #try:
        print  "Connection from ",client_address
        data = connetion.recv(1024)
        print "Receive '%s'" % data
    #finally:      
        #print "Receive '%s'" % data
        #connetion.close()