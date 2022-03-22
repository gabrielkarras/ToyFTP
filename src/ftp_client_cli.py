"""
COEN 366 TCP Client
"""
from socket import *
import click

@click.command()

# CLIENT_IPV4 = '192.168.0.12'
# CLIENT_PORT = 12000
# 
# # Setting client-side socket
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((CLIENT_IPV4, CLIENT_PORT))
# 
# # Sending name to server
# name = input("Enter name: ")
# clientSocket.send(name.encode())
# 
# # Fetching response from server
# response = clientSocket.recv(1024)
# print("From Server:", response.decode())
# clientSocket.close()