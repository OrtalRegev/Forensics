import subprocess
import socket
SERVER_PORT = 4444
SERVER_IP= '127.0.0.1'
OUTPUT_FILE = 'path=$HOME/ram.raw'
def start_comunication():

    # Create a TCP/IP socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to remote computer 80

    server_address = (SERVER_IP, SERVER_PORT)

    sock.connect(server_address)

    # Sending data to server

    data=open(OUTPUT_FILE,'r')


    sock.sendall(data.encode())

    # Receiving data from the server

    server_msg = sock.recv(1024)

    server_msg = server_msg.decode()

    # Closing the socket

    sock.close()

def terminal_command():
    command = 'insmod'
    lime_file_path = 'LiME/src/lime-4.15.0-kali2-amd64.ko'
    format_type = 'raw'
    subprocess.run([command,lime_file_path,"{0} format={1}".format(OUTPUT_FILE, format_type)])


if __name__ == '__main__':
    terminal_command()

