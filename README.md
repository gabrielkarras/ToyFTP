# ToyFTP

A simplified FTP command line application

## Setup

- ensure you have Python 3(recommended version 3.8+) and pip
- git clone https://github.com/gabrielkarras/ToyFTP.git
- activate Python virtual environment(optional, but recommended)
  - The command depends on your OS and terminal environment
  - ex: $python3 -m venv "your_venv_directory" (Bash)
- pip install --editable .

## Commands

- test: Opens ToyFTP connection with server
- put: Transfer a file to server
- get: Retrieve a file from server
- change: Change file name from server
- bye: Closes ToyFTP connection with server
- --help: to receive further information and can also be appended to any command

## Note(s)

- If you wish, you may enter your IP address and port number in lines 11-12 of ftp_server.py and lines 12-13 of ftp_client_cli.py. This will avoid the need to add the arguments --ip and --port
- You may test this with Mininet, where a host of choice can run the server script, while another host can make requests to the server.
- Tested on Windows 10 and on Ubuntu 20.04.4
- The IP address in the examples below is based off of the Mininet's generated IP addresses

## Example

- To get started you will need 2 terminals open(we're assuming a Bash terminal)
- To run the server
  - $cd src/tests/
  - $python ftp_server.py
  - server will prompt for IP address(if you leave it empty it will set the default IP address)
    - example: 10.0.0.1
  - server will prompt for port number(if you leave it empty it will set the default port number)
    - example: 12000
  - server will notify that it is up and ready
- To run the client
  - $cd src/
  - $FTPClient --help
    - help display
  - If ever you need help with a particular command, simply append "--help"
    - $FTPClient put --help
  - $FTPClient --ip "your_server_ip" -- port your_port_number --debug 1 test
    - If the setup was done correctly, we should a "success" reply from the server
  - $FTPClient --ip "10.0.0.1" -- port 12000 get
    file1.txt - We should see file1.txt appear in ./src/
  - $FTPClient --ip "10.0.0.1" -- port 12000 put
    file2.txt - We should see file2.txt in ./src/tests/
  - $FTPClient --ip "10.0.0.1" -- port 12000 change file2.txt file3.txt
    - We should see file3.txt in ./src/tests/ and file2.txt should not be there
  - $FTPClient --ip "10.0.0.1" -- port 12000 bye
    - We should see an ACK from the server and the server will exit
