"""
Toy FTP Server
"""
import re
from socket import *

DEFAULT_SERVER_IPV4 = '192.168.0.12'
DEFAULT_SERVER_PORT = 12000

def main():
    # prompt user with server's IP address and port
    server_ipv4 = input("Enter server IPv4 address: ")
    server_port = input("Enter server port: ")

    if server_ipv4 == '':
        server_ipv4 = DEFAULT_SERVER_IPV4

    if server_port == '':
        server_port = DEFAULT_SERVER_PORT
    server_port = int(server_port)

    # Server side socket set up
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((server_ipv4, server_port))
    serverSocket.listen(1) # enable
    print("Server Up and Ready!")

    # defining messages and opcodes
    Hello = 'hello'
    Bye   = 'bye'

    while True:

        connectionSocket, addr = serverSocket.accept()
        request = connectionSocket.recv(1024).decode()

        print('Request content from client')
        print(request)
        
        opcode = request[0:3]

        if '000' in opcode:
            print('put')
        
        if '001' in opcode:
            print('get')

        if '010' in opcode:
            print('change')

        if '011' in opcode:
            reply = 'success'
            connectionSocket.send(reply.encode())
        
        if '100' in opcode:
            reply = "ok"
            connectionSocket.send(reply.encode())
            print("Server is closing down!")
            connectionSocket.close()
            exit()

if __name__ == '__main__':
    main()