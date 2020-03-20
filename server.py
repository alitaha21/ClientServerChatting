# Importing the libraries of socket threading and gui
from socket import * 
from tkinter import *
from _thread import *

# Obtaining a socket object
socketObj = socket(AF_INET, SOCK_STREAM)

# Server host and port specifications
host = "127.0.0.1"
port = 8080

# Binding and assigning a listening limit
socketObj.bind((host , port))
socketObj.listen(5) 

# GUI part where i get a gui object from the library and start shaping my frame size
gui = Tk()
gui.title("Server: administrator")
gui.geometry("300x100")

# This is the label where the message will appear
label = Label(gui)
label.grid(row =3 , column=3)

# The text field in which the user will enter data
entry = Entry(gui , width="50")
entry.grid(row =1 , column =3)

sessions = []

# A submitting function that sends the data that is written in the text field upon clicking on the button
def submit():
	message = "Server: " + entry.get()
	for i in sessions:
		i.send(message.encode('utf-8'))
	entry.delete(0 , END)

# A submitting button
btn = Button(gui , text = "Send" , bg ="blue" , fg = "black" , width =7 , height =1 , command=submit)
btn.grid(row=2 , column=3)

# A threading function shows the info of the sender and the message that was sent
def dataReceivingThread(clientsocket, address):
	while True:
		label["text"]= "Client with address: " + str(address) +" sent: " + clientsocket.recv(1024).decode('utf-8')
		
# Accepting the client socket and the address then appending it to our session and starting a new thread
def mainTread(socketObj):
	while True:
		clientsocket , address = socketObj.accept()
		sessions.append(clientsocket)

		label["text"] = "New connection from: " + str(address)
		start_new_thread(dataReceivingThread, (clientsocket, address))
start_new_thread(mainTread , (socketObj,))

gui.mainloop()