#Name - Omkar Shrikant Gawade
#ID - 1001967237
import os
global host
host = "127.0.0.1" #declared a global variable to be accessed by anywhere in functions

def conn_b():
    import socket
    os.chdir(r"path/to/server_a_directory") #hard coded directory address
    list_a = os.popen(str("ls -l | awk '{print $9, $8, $7, $6, $5}'")).read() #directory "a" listing
    port = 31334
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #starting and stoting TCP socket connection
    socket.connect((host, port))
    list_b = socket.recv(1024).decode() #received directory b listing
    socket.close()

    list = list_a + list_b #concatinate both lists
    list = sorted(list.splitlines()) #sorting concatinated list
    del list[0:2] #removing blank spaces
    return list

def server_a():
    import socket
    port = 31333
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((host, port))
    socket.listen(1)
    print("Socket Successfully Created For ServerA...!!")
    while True:
        conn, addr = socket.accept()
        if conn:
            final_list = conn_b() #due to connection with client a connection to function b is called
            conn.send(str(final_list).encode()) #send both directory listing to client
            break
    socket.close()
server_a()
