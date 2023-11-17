import socket
import sys

HEADER = 64
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
PORT = None
ADDR = tuple()
DISCONNECT_MESSAGE = '!DISCONNECT'


def set_port():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <PORT>")
        sys.exit(1)
    else:
        global PORT, ADDR
        PORT = int(sys.argv[1])
        ADDR = (SERVER, PORT)


set_port()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
