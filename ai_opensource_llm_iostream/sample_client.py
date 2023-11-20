import socket
import sys

HEADER = 1024
FORMAT = 'utf-8'

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5050
SERVER_ADDR = (SERVER_IP, SERVER_PORT)

CLIENT_IP = socket.gethostbyname(socket.gethostname())
CLIENT_PORT = None
CLIENT_ADDR = tuple()

DISCONNECT_MESSAGE = '!DISCONNECT'


def set_port():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <PORT_Client>")
        sys.exit(1)
    else:
        global CLIENT_PORT, CLIENT_ADDR
        CLIENT_PORT = int(sys.argv[1])
        CLIENT_ADDR = (CLIENT_IP, CLIENT_PORT)


set_port()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(CLIENT_ADDR)
client.connect(SERVER_ADDR)
print(f' Connected to {SERVER_ADDR} '.center(40, '-'))


def send(msg:str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if not (msg.strip().upper() == 'QUIT'):
        print(client.recv(2048).decode(FORMAT))


while True:
    msg = input('>> ')
    send(msg)
    if msg.strip().upper() == 'QUIT':
        break


