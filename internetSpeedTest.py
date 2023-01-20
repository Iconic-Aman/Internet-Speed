from tkinter import *  #tkinter module is used for GUI(graphics user interface) in python 

import speedtest
def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    up = str(round(sp.upload()/(10**6),3)) + "Mbps"
    lab_down.config(text = down)
    lab_up.config(text = up)


# make a variable and call the tkinter class
sp = Tk()
sp.title("Internet Speed Test")  #change title
sp.geometry("500x500")  #change the height and width of window
sp.config(bg="#98F5FF") #config function is used for decoration

lab = Label(sp,text="Internet Speed Test", font= "TimesnewRoman 20 bold", bg="#98F5FF" )  #Helvetica
lab.place(x=100, y=40, height=40, width= 300)

lab = Label(sp,text="Download speed", font=("Helvetica",18,"bold",), bg="#98F5FF" )  #Helvetica
lab.place(x=100, y=100, height=40, width= 300)

lab_down = Label(sp,text="00", font=("Helvetica",18,"bold",), bg="#98F5FF" )  #Helvetica
lab_down.place(x=100, y=135, height=40, width= 300)

lab = Label(sp,text="Upload speed", font=("Helvetica",18,"bold",), bg="#98F5FF" )  #Helvetica
lab.place(x=100, y=190, height=40, width= 300)

lab_up = Label(sp,text="00", font=("Helvetica",18,"bold",), bg="#98F5FF" )  #Helvetica
lab_up.place(x=100, y=225, height=40, width= 300)

button = Button(sp, text="check", font=("Helvetica",18,"bold"), bg="red", command=speedCheck)
button.place(x=200, y=300, height=40, width= 100,)


sp.mainloop() #make a square window for GUI


