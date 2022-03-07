import simpleaudio as sa
from tkinter import *

def playringtone():
    filename = 'discord_ringtone.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()

    def stopsound():
        play_obj.stop()
	top.destroy()

    top = Tk()
    top.geometry("500x300")
    b = Button(top, text = "stop", command = stopsound)
    b.pack()
    top.mainloop()


####################################################################################

import socket


UDPserversocket= socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)

UDPserversocket.bind(("0.0.0.0", 8080))

print("socket is listening...")

while True:
    bytesAdressPair = UDPserversocket.recvfrom(1024)
    message = bytesAdressPair[0]
    adress = bytesAdressPair[1]

    print(message, adress)
    
    message = str(message).split("b",1)[1]
    print(message)
    if message == "'PlaySound'":
        playringtone()	


