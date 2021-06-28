import socket
import threading #for multithreading

PORT = 5000 
SERVER = socket.gethostbyname(socket.gethostname()) #automatically get the local IP Address of the computer to run the server
ADDRESS = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making a new socket
server.bind(ADDRESS) #bind the socket to the address

def handle_client(con, address):
    print(f"[NEW CONNECTION] {address} connected.")

    connected = True
    while connected:
        msg_len = con.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = con.recv(msg_len).decode(FORMAT) #tells how long the message is going to be

            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{address}] {msg}")
            con.send("Message received.".encode(FORMAT)) #send a message back to client

    con.close()


def start():
    server.listen()
    print(f"[LISTENING] Listening to connection on {SERVER}") #tells which address the server is listening to
    while True:
        connect, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connect, address))
        thread.start() #start a new thread for the handle_client function
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #the active threads except the one listening for connections

print("[STARTING] starting the server...")
start()