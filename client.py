import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
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
    print(client.recv(2048).decode(FORMAT)) #Uses a large number to make sure it's able to recieve a message, and decoded so it's not in byte format

send("Hello World")
input()
send("Hello Everyone!")
input()
send("Hello Gadtardi!")

send(DISCONNECT_MESSAGE)  