#import socket module for establishing socket 
import socket

#establishing socket connection
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#fetching host name
Host_Name=socket.gethostname()
Port=5000

#connecting client to server
server.connect((Host_Name,Port))

while True:
    #receiving message from server
    message_from_server=server.recv(100)
    print("Server : ",message_from_server.decode('utf-8'))
    #sending message to server
    message=input("Client : ")
    message_to_server=server.send(bytes(message,'utf-8'))
