import socket

PORT = 5000
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnected"
SERVER =  socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS) #connecting to the server

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len)) #pad the message so it is the same as HEADER
    client.send(send_len)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

send("MAMAAAAAAAAA OOOOOOOOHHHHHH")
input()
send("OH MAI GAH")
send(DISCONNECT_MSG)