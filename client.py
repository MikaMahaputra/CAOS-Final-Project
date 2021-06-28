import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) #Encodes the string into byte like format
    msg_length = len(message) #Get the length
    send_length = str(msg_length).encode(FORMAT) #Encode as a string
    send_length += b' ' * (HEADER - len(send_length)) #Make sure it's padded to 64 bit
    client.send(send_length)
    client.send(message)

    send("Hello World")