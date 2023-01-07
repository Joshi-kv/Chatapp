#import socket module for establishing socket 
import socket

#establishing socket connection
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#fetching host name
Host_Name=socket.gethostname()
Port=5000

#binding hostname and port
server.bind((Host_Name,Port))
server.listen(4)

#accepting client ip address
client,address=server.accept()
while True:
    #sendiing message to client
    message=input('Server : ')
    client.send(bytes(message,'utf-8'))
    #receiving message from client.
    message_from_client=client.recv(100)
    print("Client : ",message_from_client.decode('utf-8'))