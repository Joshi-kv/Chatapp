#import socket module for establishing socket 
import socket

#import tkinter module.
from tkinter import *

#function to send message
def send(messagebox,entry):
    #sendiing message to client
    message=entry.get()
    messagebox.insert('end','Server : '+message)
    entry.delete(0,END)  
    client.send(bytes(message,'utf-8'))
    
#function for receiving message
def receive(messagebox):
     message_from_client=client.recv(100)
     messagebox.insert('end','Client : '+message_from_client.decode('utf-8'))
         
root=Tk()
root.title('Server')
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

#binding hostname and port
server.bind((Host_Name,Port))
server.listen(4)

#accepting client ip address
client,address=server.accept()
root.mainloop()