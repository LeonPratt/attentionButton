import simpleaudio as sa
from tkinter import *
import tkinter as tk
import threading
import traceback
import pdpyras
from decouple import config
#print("C:Usersleona\\attention_button_startup\discord_ringtone.wav")

Key = config('APIKEY')
RoutingKey = config('RoutingKEY')


global API_session
global event_session
event_session = pdpyras.EventsAPISession(RoutingKey)
API_session = pdpyras.APISession(Key)
try:
    spltrequest = ""



    def playringtone(incident_key):
        soundstopped = False
        filename = r"C:\Users\leona\attention_button_startup\discord_ringtone.wav"
        wave_obj = sa.WaveObject.from_wave_file(str(filename))
        event_session.resolve(incident_key)
        playobj = wave_obj.play()
            
        def stopsound():
            playobj.stop()
            top.destroy()
            soundstopped = True
        top = Tk()
        top.geometry("500x300")

        txt = "stop \n %s" %request.split(":")[1]
        b = Button(top, text = txt , command = stopsound)
        b.pack()
        top.mainloop()


    ####################################################################################

    import socket


    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8080
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)
    f = open("debug.txt","w")

    f.writelines("opened socket")
    f.close()

    while True:   
        # Wait for client connections

        client_connection, client_address = server_socket.accept()
        print(client_address)
      
        f = open("debug.txt","w")

        f.writelines("recieved packets")
        f.close()

        # Get the client request


        request = client_connection.recv(1024).decode()
        print("sefsfefsf",request)
        spltRequest = request.split(":")
        print("spltrequest = ", spltRequest)
        incident_KEY = spltRequest[2]
        print(incident_KEY)
        if spltRequest[0] == "PlaySound":
            client_connection.sendall(request.encode())
            playingsound = threading.Thread(target=playringtone(incident_KEY))
            playingsound.start()


        client_connection.close()
        f = open("debug.txt","w")

        f.writelines("connection closed")
        f.close()

        #bytesAdressPair = s.recvfrom(1024)
        #message = bytesAdressPair[0]
        #adress = bytesAdressPair[1]
    #
        #print(message, adress)
        #
        #message = str(message).split("b",1)[1]
        #print(message)
        #if message == "'PlaySound'":
        #    playringtone()	

except Exception as e:
        print(e)
        f = open("debug.txt","w")

        traceback.print_exc(file=f)
    
        f.close()




