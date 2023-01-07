#import socket module for establishing socket 
import socket
#import tkinter module.
from tkinter import *

#function to send message
def send(messagebox,entry):
    #sendiing message to client
    message=entry.get()
    messagebox.insert('end','Client : '+message)
    entry.delete(0,END)  
    server.send(bytes(message,'utf-8'))
    
#function for receiving message
def receive(messagebox):
     message_from_server=server.recv(100)
     messagebox.insert('end','Server : '+message_from_server.decode('utf-8'))
         
root=Tk()
root.title('Client')
entry=Entry()
entry.pack(side=BOTTOM)
messagebox=Listbox(root,width=100)
messagebox.pack()
send_button=Button(root,text="Send",command=lambda:send(messagebox,entry))
send_button.pack(side=BOTTOM)
receive_button=Button(root,text="Receive",command=lambda:receive(messagebox))
receive_button.pack(side=BOTTOM)
#establishing socket connection
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#fetching host name
Host_Name=socket.gethostname()
Port=5000

#connecting client to server
server.connect((Host_Name,Port))
root.mainloop()