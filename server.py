import socket #importing python socket library
import threading #importing python threading library

HEADER = 64 #defining header length in bytes
PORT = 6050 # pick port
#SERVER = "192.168.1.5" # manual own local ip definition
SERVER = socket.gethostbyname(socket.gethostname()) # using gethostbyname to get own local ip
#print("server starting on address: " + SERVER) # debugging
ADDR = (SERVER, PORT) # socket address
FORMAT = 'utf-8' #formatter
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket creation and type
server.bind(ADDR) # binding socket


def handle_client(conn, addr): #client handler function
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)#decoding the message into readable form by program
        if msg_length:
            msg_length = int(msg_length) #turning message length into an int
            msg = conn.recv(msg_length).decode(FORMAT) #decoding actual message
            if msg == DISCONNECT_MESSAGE: #if client disconnects
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("msg received".encode(FORMAT)) #confirmation msg to client

    conn.close() #terminates connection

def start(): #server starter function
    server.listen() #listen for new connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #get the address of the connection, conn to store info about the client
        thread = threading.Thread(target=handle_client, args=(conn, addr))# new thread to run handle_client
        thread.start()
        print(f"[ACTIVE CONNECTIONS {threading.activeCount() - 1}") # counts number of threads per new client so we also know number of clients from number of threads  (-1 to discount the start thread)

print("[STARTING] server is starting...")
start()

