#Name - Omkar Shrikant Gawade
#ID - 1001967237
import socket
import os

os.chdir(r"path/to/server_b_directory") #changing directory to retrieve directory_b lisitng
list_b = os.popen(str("ls -l | awk '{print $9, $8, $7, $6, $5}'")).read().encode() #directory "b" listing

host = "127.0.0.1"
port = 31334

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen(1)
print("Socket Successfully Created For ServerB...!!")
while True:
    conn, addr = socket.accept()
    conn.send(list_b) #send directory "b" listing over connection
    break
    conn.close()
