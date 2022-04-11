"""
Toy FTP Server

Author: Gabriel Karras
"""
from socket import *
import os

DEFAULT_SERVER_IPV4 = '192.168.0.12'
DEFAULT_SERVER_PORT = 12000

FILE_NAME_LIMIT = 32 # file name with less than 32 characters in total
FILE_SIZE_LIMIT = 536870912 # specified by 4 bytes/2^32 bits/ 2^29 bytes


def get_size(file):
    """
    Returns the file size
    """
    size = os.stat(file)
    return size.st_size


def main():

    # prompt user with server's IP address and port
    serverIPv4 = input("Enter server IPv4 address: ")
    serverPort = input("Enter server port: ")

    if serverIPv4 == '':
        serverIPv4 = DEFAULT_SERVER_IPV4

    if serverPort == '':
        serverPort = DEFAULT_SERVER_PORT
    serverPort = int(serverPort)

    # Server side socket set up
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverIPv4, serverPort))
    serverSocket.listen(1) # enable
    print("Server Up and Ready!")

    while True:

        connectionSocket, addr = serverSocket.accept()
        request = connectionSocket.recv(1024).decode()

        print('Request message: ')
        print(request)

        request_fields = request.split(',')
        opcode = request_fields[0]

        if '000' in opcode:
            # put request
            fileNameLength = request_fields[1]
            fileName = request_fields[2]
            fileSize = request_fields[3]
            filePayload = request_fields[4]

            if (fileSize < FILE_SIZE_LIMIT and fileNameLength < FILE_NAME_LIMIT):
                if ( not os.path.exists(fileName) ):
                    with open(fileName, "w") as f:
                        f.write(filePayload)
                    reply = "000"
                    connectionSocket.send(reply.encode())
                else:
                    print("Error: File already exists")
                    reply = "111"
                    connectionSocket.send(reply.encode())
            else:
                print("Error: file exceeds file size limit or character limit")
                reply = "111"
                connectionSocket.send(reply.encode())  

        elif '001' in opcode:
            # get request
            fileNameLength = request_fields[1]
            fileName = request_fields[2]
            
            if fileNameLength < FILE_NAME_LIMIT:
                try:    
                    file_data = open(fileName, 'r').read()

                    reply_opcode = "001"
                    reply_file_name_length = str(len(fileName))
                    reply_file_size = str(get_size(file_data))

                    reply = reply_opcode + ',' + reply_file_name_length + ',' + reply_file_size + ',' + file_data
                    connectionSocket.send(reply.encode())
                except (OSError, IOError) as e:
                    reply = "010" # File not found
                    connectionSocket.send(reply.encode())
                    print("Error during get request:" + e)
            else:
                print("File exceeds character limit")
                reply = "010" 
                connectionSocket.send(reply.encode())

        elif '010' in opcode:
            # change request
            oldFileNameLength = request_fields[1]
            oldFileName = request_fields[2]
            newFileNameLength = request_fields[3]
            newFileName = request_fields[4]

            if (oldFileNameLength < FILE_NAME_LIMIT and newFileNameLength < FILE_NAME_LIMIT):
                os.rename(oldFileName, newFileName)
                reply = "000"
                connectionSocket.send(reply.encode())
            else:
                reply = "100" # failed get request
                connectionSocket.send(reply.encode())

        elif '011' in opcode:
            # test connection request
            reply = 'success'
            connectionSocket.send(reply.encode())
        
        elif '100' in opcode:
            # shut down request
            reply = "ok"
            connectionSocket.send(reply.encode())
            print("Server is closing down!")
            connectionSocket.close()
            exit()
        else:
            print("Error: unknown request")
            reply = "101"

if __name__ == '__main__':
    main()