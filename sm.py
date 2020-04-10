from Tkinter import *
from time import *
import os


cmd='config.bat '
tskend='taskkill /F /IM python.exe /T'


master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
   xmr=e.get()
   print xmr
   os.system(cmd+xmr)
start = Button(master, text="Start mining", width=10, command=callback)
start.pack()
stop = Button(master, text="Stop MinIng", width=10, command=tskend)
stop.pack()



mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()



text = content.get()
content.set(text)
