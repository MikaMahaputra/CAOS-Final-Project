import socket 
import threading #A way of creating a multiple thread in one python program

HEADER = 64 #Sets the length of the message
PORT = 5050 #Trying to pick a port that's not used by something else
SERVER = socket.gethostbyname(socket.gethostname()) #Get the IP address automatically
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Sending data through stream and over the internet
server.bind(ADDR) #Binding the socket to this address

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #Decode from it's byte using utf-8
        if msg_length:
            msg_length = int(msg_length) #Converting to intreger
            msg = conn.recv(msg_length).decode(FORMAT) #Actual message
            if msg == DISCONNECT_MESSAGE:
                connected = False
        print(f"[{addr}] {msg}")
        conn.send("Message received".encode(FORMAT))
    conn.close()

def start():
    server.listen() #Listening for new connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #When a new connection occurs it'll store the address of that connection
        thread = threading.Thread(target= handle_client, args =(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #Tells how many threads are active

print("[STARTING] Starting the server...")
start()