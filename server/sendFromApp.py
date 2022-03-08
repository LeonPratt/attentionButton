import socket
from tkinter import *
import tkinter as tk
from tkinter import ttk

from matplotlib.pyplot import text
roomname = ""


def getRoom():


    master = tk.Tk()
    tk.Label(master, text="room name").grid(row=0)


    e1 = tk.Entry(master)


    e1.grid(row=0, column=1)


    master.mainloop()
#getRoom()

def send():
    
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

