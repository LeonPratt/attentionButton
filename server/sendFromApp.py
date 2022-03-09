import socket

from tkinter import *

import tkinter as tk

from tkinter import ttk




r=""

while True:
	
	
 def send(roomname):
	
    
	
     room = bytes(roomname, encoding="utf-8")
	
     message = b"PlaySound:" + room
	
     TCP_IP = "192.168.1.20"
	
     TCP_PORT = 8080
	
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
     s.connect((TCP_IP, TCP_PORT))
	
     s.send(message)
	
     data = s.recv(1024)
	
     s.close()
	
     print("recieved:", data)
	
  
	
 root= tk.Tk()
	
  
	
 canvas1 = tk.Canvas(root, width = 400, height = 300, relief = 'raised')
	
 canvas1.pack()
	
  
	
 label1 = tk.Label(root, text='send notification')
	
 label1.config(font=('helvetica', 14))
	
 canvas1.create_window(200, 25, window=label1)
	
  
	
 label2 = tk.Label(root, text='enter room name:')
	
 label2.config(font=('helvetica', 10))
	
 canvas1.create_window(200, 100, window=label2)
	
  
	
 entry1 = tk.Entry (root)
	
 canvas1.create_window(200, 300, window=entry1)
	
 
	
 def getSquareRoot ():
	
    
	
     r = entry1.get()
	
     send(r)
	
    
	
    
	
 button1 = tk.Button(text='confirm room name', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'), pady =-90)
	
 canvas1.create_window(200, 180, window=button1)
	
  
	
 root.mainloop()