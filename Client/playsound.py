import simpleaudio as sa
from tkinter import *


#print("C:Usersleona\\attention_button_startup\discord_ringtone.wav")

def playringtone():
    soundstopped = False
    filename = r"C:\Users\leona\attention_button_startup\discord_ringtone.wav"
    wave_obj = sa.WaveObject.from_wave_file(str(filename))

    playobj = wave_obj.play()
        
    def stopsound():
        playobj.stop()
        top.destroy()
        soundstopped = True
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


