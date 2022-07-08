#Name - Omkar Shrikant Gawade
#ID - 1001967237
import socket
import os

host = "127.0.0.1"
port = 31333

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket
socket.connect((host, port)) #making socket connection to server_a
data = socket.recv(1024).decode() #recived both directory listing

for i in data.split(','): #printing file
    print(i)
socket.close() #closing socket connection
