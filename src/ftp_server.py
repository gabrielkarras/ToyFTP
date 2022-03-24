"""
Toy FTP Server
"""
from ast import match_case
import re
from socket import *

# DEFAULT_SERVER_IPV4 = '192.168.0.12'
# DEFAULT_SERVER_PORT = 12000

# prompt user with server's IP address and port
server_ipv4 = input("Enter server IPv4 address: ")
server_port = input("Enter server port: ")
 
# Server side socket set up
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((server_ipv4,server_port))
serverSocket.listen(1) # enable
print("Server Up and Ready!")

while True:
    
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024).decode()
    
    if request == 'Gabriel':
        reply = "Student"
        connectionSocket.send(reply.encode())
    else:
        reply = "Unknown or TA"
        connectionSocket.send(reply.encode())
    connectionSocket.close()
