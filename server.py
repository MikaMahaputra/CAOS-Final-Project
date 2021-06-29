import socket 
import threading

PORT = 5050 # pick port
#SERVER = "192.168.1.5" # manual own local ip definition
SERVER = socket.gethostbyname(socket.gethostname()) # using gethostbyname to get own local ip
print(SERVER) # debugging
ADDR = (SERVER, PORT) # socket address

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket creation and type
server.bind(ADDR) # binding socket





