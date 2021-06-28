import socket 
import threading #A way of creating a multiple thread in one python program

PORT = 5050 #Trying to pick a port that's not used by something else
SERVER = socket.gethostname(socket.gethostname()) #Get the IP address automatically
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Sending data through stream and over the internet
server.bind(ADDR) #Binding the socket to this address

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv()

def start():
    server.listen #Listening for new connections
    while True:
       conn, addr = server.accept() #When a new connection occurs it'll store the address of that connection
       thread = threading.Thread(target= handle_client, args =(conn, addr))
       thread.start()
       print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #Tells how many threads are active

print("[STARTING] Starting the server...")
start()