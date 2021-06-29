import socket 
import threading

PORT = 5050 # pick port
#SERVER = "192.168.1.5" # manual own local ip definition
SERVER = socket.gethostbyname(socket.gethostname()) # using gethostbyname to get own local ip
print(SERVER) # debugging
ADDR = (SERVER, PORT) # socket address

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket creation and type
server.bind(ADDR) # binding socket

def handle_client(conn, addr):
    pass

def start():
    server.listen() #listen for new connections
    while True:
        conn, addr = server.accept() #get the address of the connection, conn to store info about the client
        thread = threading.Thread(target=handle_client, args=(conn, addr))# new thread to run handle_client
        thread.start()
        print(f"[ACTIVE CONNECTIONS {threading.activeCount() - 1}") # counts number of threads per new client so we also know number of clients from number of threads  (-1 to discount the start thread)

print("[STARTING] server is starting...")
start()

