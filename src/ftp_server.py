"""
COEN 366 Server
"""
from socket import *


SERVER_IPV4 = '192.168.0.12'
SERVER_PORT = 12000

# Server side socket set up
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((SERVER_IPV4,SERVER_PORT))
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
