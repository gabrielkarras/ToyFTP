"""
Toy FTP Client
"""
from socket import *
import os
from urllib import response
import click


DEFAULT_SERVER_IPV4 = '192.168.0.12'
DEFAULT_SERVER_PORT = 12000


# Configuration object shared across commands
class Config(object):
    def __init__(self, ip=DEFAULT_SERVER_IPV4, port=DEFAULT_SERVER_PORT, debug=1, home='.'):
        self.ipv4 = ip
        self.port = port
        self.file_directory = os.path.abspath(home or '.')
        self.debug = debug


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--ip', default=DEFAULT_SERVER_IPV4, help='Server IP address')
@click.option('--port', default=DEFAULT_SERVER_PORT, help='Port number')
@click.option('--debug', default=1, help='Debug mode: 0-Off, 1-On')
@click.option('--file_dir', default= '.', help='file directory path')
@pass_config
def cli(config, ip, port, debug, file_dir):
    config.obj = Config(ip, port, debug, file_dir)


@pass_config
def send_request(config, message):
    # Setting client-side socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((config.ipv4, config.port))
    clientSocket.send(message.encode())
    
    # Fetching response from server
    response = clientSocket.recv(1024)
    decoded_response = response.decode()
    clientSocket.close()
    return decoded_response


@click.command()
@pass_config
def test(config):
    """
    Tests FTP connection with server
    """
    # Testing connection with server
    
    click.echo('test started')
    
    # Sending test message to server
    message = 'hello'
    response = send_request(message)
    if response == 'success':
        print('Response from Server:', response)
        click.echo('Connection established with server')       
    else:
        print('Response from Server: ', response)
        click.echo('Connection issues with server')
    click.echo('testing done')


@click.command()
@click.argument('file', type=click.File('rb'), default='file2.txt')
@pass_config
def put(config, file):
    """
    Transfer a file to server
    \b
    [command] [arg1]
    put        file    

    \b
    file - file name with its extension
    """
    # grab file (assumption within root project folder)
    # get filename size: basically count the number of characters
    # get file size
    # 000 + filename length + filename + file size + payload
    click.echo('put') 


@click.command()
@click.argument('file', default='file1.txt')
@pass_config
def get(config, file):
    """
    Retrieve a file from server
    
    \b
    [command] [arg1]
    get        file    

    \b
    file - file name with its extension
    """
    # grab file
    # get filename size: basically count the number of characters
    # 001+filename size+filename
    click.echo('get') 


@click.command()
@click.argument('oldfile', default='file2.txt')
@click.argument('newfile', default='file3.txt')
@pass_config
def change(config, oldfile, newfile):
    """
    Change file name from server

    \b
    [command] [ arg1 ] [ arg2 ]
    get       oldfile  newfile

    \b
    oldfile - old file name with its extension
    newfile - new file name with its extension
    """
    # grab file names
    # get filename size: basically count the number of characters
    # 010 + filename size + filename
    click.echo('change') 


@click.command()
@pass_config
def bye(config):
    """Closes FTP connection"""
    message = 'bye'
    response = send_request(message)

    if config.debug:
        if response == "ok":
                print('Response from Server: ', response)
                click.echo('Closed connection to server')
        else:
            print('Response from Server: ', response)
            click.echo('Closure issues. Might need to restart!')
    
    click.echo('bye')

# adding commands to cli
cli.add_command(test)
cli.add_command(put)
cli.add_command(get)
cli.add_command(change)
cli.add_command(bye)

if __name__ == '__main__':
    cli()
