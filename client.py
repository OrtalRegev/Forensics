import subprocess
import socket
import os

SERVER_PORT = 6969
SERVER_IP = '10.0.0.11'
OUTPUT_PATH = 'tcp:6969'
FORMAT_TYPE = 'raw'
LIME_FILE_PATH = 'LiME/src/lime-4.15.0-kali2-amd64.ko'
sock = None  # The socket


def find_lime_file():
    global LIME_FILE_PATH
    for root, dirs, files in os.walk("LiME/src/"):
        for file in files:
            if file.endswith(".ko"):
                LIME_FILE_PATH = os.path.join(root, file)


def start_communication():
    global sock
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connecting to remote computer
    try:
        sock.connect((SERVER_IP, SERVER_PORT))
    except Exception as e:
        print("Cannot connect to the server:", e)


# Dumping file using LiME
def terminal_command():
    command = 'insmod'
    subprocess.call([command, LIME_FILE_PATH, "path={0} format={1}".format(OUTPUT_PATH, FORMAT_TYPE)])


def send_to_server(message):
    # Sending data to server
    sock.send(message)


def close_communication():
    sock.close()


def receive_from_server(size):
    # Receiving data from the server
    server_msg = sock.recv(size)
    return server_msg.decode()


if __name__ == '__main__':
    find_lime_file()
    terminal_command()





