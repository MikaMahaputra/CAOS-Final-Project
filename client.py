import socket

PORT = 5000
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER =  "127.0.1.1"
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS) #connecting to the server