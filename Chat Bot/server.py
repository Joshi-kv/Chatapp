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

#establishing connection to client
while True:
    #accepting client ip address
    client,address=server.accept()
    print('Client connected successfully to address',address)