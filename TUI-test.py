import tkinter
from tkinter import *
import subprocess
import os
from os import system as cmd

def test():
    os.system('sudo xterm -into %d -geometry 100x28 -sb -e overscan &' % terminfo)

def sysinfo():
    os.system('xterm -into %d -geometry 100x28 -sb -e systeminfo &' % terminfo)

def ipconf():
    os.system('xterm -into %d -geometry 51x11 -sb -e ipconfig &' % terminfo)

def Uninstall():
    os.system('sudo xterm -into %d -geometry 100x28 -sb -e TBuninstall &' % terminfo)

WINDOW_SIZE = "1024x768"
top = tkinter.Tk()
top.geometry(WINDOW_SIZE)

Button1  = tkinter.Button(top, text ="Systeem informatie opvragen", command=sysinfo)
Button1.pack()

Button2  = tkinter.Button(top, text ="IP adres achterhalen", command = ipconf)
Button2.pack()

Button3  = tkinter.Button(top, text ="Zwarte balken weghalen", command = test)
Button3.pack()

Button4 = tkinter.Button(top, text = "Tools Verwijderen", command = Uninstall)
Button4.pack()

termin = Frame(top, height=1000, width=1000)

termin.pack(fill=BOTH, expand=YES)
terminfo = termin.winfo_id()


def send_entry_to_terminal(*args):
    cmd("%s" % (BasicCovTests))

if __name__ == "__main__":
    top.title('KEUZE MENU')
    top.mainloop()
