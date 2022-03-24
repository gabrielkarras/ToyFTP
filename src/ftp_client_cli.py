"""
Toy FTP Client
"""
from socket import *
import click

# CLIENT_IPV4 = '192.168.0.12'
# CLIENT_PORT = 12000
 
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

# Configuration object shared across commands
class Config(object):
    def __init__(self):
        pass

pass_config = click.make_pass_decorator(Config)

@click.group()
def cli():
    pass

@click.command()
#@click.option()
#@click.argument()
def start():
    click.echo('start')    

@click.command()
def put():
    click.echo('put') 

@click.command()
def get():
    click.echo('get') 

@click.command()
def change():
    click.echo('change') 

@click.command()
def bye():
    click.echo('bye')

@click.command()
def help():
    click.echo('start: Opens ToyFTP connection with server'     )
    click.echo('put: Transfer a file to server'                 )
    click.echo('get: Retrieve a file from server'               )
    click.echo('change: Change file name from server'           )
    click.echo('bye: Closes ToyFTP connection with server'      )
    click.echo('help: Prints out descriptions of all commdands ')

# adding commands to cli
cli.add_command(start)
cli.add_command(put)
cli.add_command(get)
cli.add_command(change)
cli.add_command(bye)
cli.add_command(help)

if __name__ == '__main__':
    cli()
