import socket
import threading
from typing import Tuple

from userthreads.userthreads import UserThreads

HEADER = 1024
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = 'QUIT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

User_Threads = UserThreads()


def handle_client(conn: socket, addr: Tuple[str, int]):
    print(f"[NEW CONN] Address {addr} connected")

    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                print(f"[{addr}] {msg}")
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[{addr}] Disconnecting...")
                    conn.send("Disconnecting...".encode(FORMAT))
                else:
                    response = User_Threads.chat(addr, msg)
                    conn.send(response.encode(FORMAT))
        except ConnectionResetError:
            # Handle connection reset error (client forcibly closed the connection)
            print(f"[{addr}] Connection reset by client.")
            connected = False

    conn.close()
    print(f"[{addr}] Connection closed.")


def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}:{PORT}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONN] {threading.active_count() - 1}')


print("[STARTING] Server is starting...")
start()
