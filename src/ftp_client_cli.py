"""
Toy FTP Client
"""
# import re
from socket import *
import os
# from urllib import response
import click


DEFAULT_SERVER_IPV4 = '192.168.0.12'
DEFAULT_SERVER_PORT = 12000

CHARACTER_LIMIT = 32


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
    clientSocket.close()
    return response.decode()


def get_size(file):
    size = os.stat(file)
    return size.st_size


@click.command()
@pass_config
def test(config):
    """
    Tests FTP connection with server
    """
    # Testing connection with server
    
    click.echo('test started')
    
    # Sending test message to server
    request = '011'
    response = send_request(request)
    if response == 'success':
        print('Response from Server:', response)
        click.echo('Connection established with server')       
    else:
        print('Response from Server: ', response)
        click.echo('Connection issues with server')
    click.echo('testing done')


@click.command()
@click.argument('file', default='file2.txt')
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
    char_count = len(file)
    if char_count < CHARACTER_LIMIT:
        opcode = '000'
        filename_length = str(char_count)
        file_name = str(file)
        file_size = str(get_size(file))
        header = opcode + filename_length + file_name + file_size    

        data = open(file, 'r').read()
        request = header + data
        
        send_request(request)
    else:
        click.echo('File name exceeds 31 character limit!')
        exit()


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
    char_count = len(file)
    if char_count < CHARACTER_LIMIT:
        opcode = '001'
        filename_length = str(char_count)
        file_name = str(file)
        request = opcode + filename_length + file_name
        send_request(request)
    else:
        click.echo('File name exceeds 31 character limit!')
        exit()


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
    char_count_oldfile = len(oldfile)
    char_count_newfile = len(newfile)
    if char_count_oldfile < 32 and char_count_newfile < 32 :
        opcode = '010'
        old_filename_length = str(char_count_oldfile)
        old_file_name = str(oldfile)
        new_filename_length = str(char_count_newfile)
        new_file_name = str(newfile)
        request = opcode + old_filename_length + old_file_name + new_filename_length + new_file_name
        send_request(request)
    else:
        click.echo('File name exceeds 31 character limit!')
        exit() 


@click.command()
@pass_config
def bye(config):
    """Closes FTP connection"""
    request = '100'
    response = send_request(request)

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
