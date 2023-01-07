#import socket module for establishing socket 
import socket

#establishing socket connection
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#fetching host name
Host_Name=socket.gethostname()
Port=5000

#connecting client to server
server.connect((Host_Name,Port))

#receiving message from server
message=server.recv(100)
print(message.decode('utf-8'))