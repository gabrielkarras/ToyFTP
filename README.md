# ToyFTP

A simplified FTP command line application

## Setup

- ensure you have Python 3(recommended version 3.9+)
- git clone https://github.com/gabrielkarras/ToyFTP.git
- activate Python virtual environment(optional, but recommended)
    - The command depends on your OS and terminal environment
- pip install --editable .

## Commands

- test: Opens ToyFTP connection with server
- put: Transfer a file to server
- get: Retrieve a file from server
- change: Change file name from server
- bye: Closes ToyFTP connection with server
- --help: to receive further information for a command

## Example

- You will need 2 terminals open
- To run the server
   - $cd src/tests/
   - $python ftp_server.py
   - server will prompt for IP address(if you leave it empty it will set the default IP address)
   - server will prompt for port number(if you leave it empty it will set the default port number)
   - server will prompt that it is up and ready
- Client command examples
    - $cd src/
    - $FTPClient --help
        - help display
    - $FTPClient --ip "your_server_ip" -- port your_port_number --debug 1 test
        - If the setup was done correctly, we should a "success" reply from the server
    - $FTPClient --ip "your_server_ip" -- port your_port_number get 
    file1.txt
        - We should see file1.txt appear in ./src/
    - $FTPClient --ip "your_server_ip" -- port your_port_number put 
    file2.txt
        - We should see file2.txt in ./src/tests/
    - $FTPClient --ip "your_server_ip" -- port your_port_number change file2.txt file3.txt
        - We should see file3.txt in ./src/tests/ and file2.txt should not be there
    - $FTPClient --ip "your_server_ip" -- port your_port_number bye
        - We should see an ACK from the server and the server will exit

## Note(s)
-  If you wish, you may enter your IP address and port number in lines 11-12 of ftp_server.py and lines 12-13 of ftp_client_cli.py. This will avoid the need to add the arguments --ip and --port

- You may test this with Minine, where a host of choice can run the server script, while another host can make requests to the server.