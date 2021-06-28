import socket
import threading #for multithreading

PORT = 5000 
SERVER = socket.gethostbyname(socket.gethostname()) #automatically get the local IP Address of the computer to run the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making a new socket

