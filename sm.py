from Tkinter import *
import os
import subprocess


cmd='config.bat '



master = Tk()

e = Entry(master)
e.pack()

e.focus_set()
def taskend():
   subprocess.call("taskkill /f /im xmrig.exe", shell=True)
   quit()

def callback():
   xmr=e.get()
   print xmr
   subprocess.Popen(cmd+xmr)
start = Button(master, text="Start mining", width=10, command=callback)
start.pack()
stop = Button(master, text="Stop Mining", width=10, command=taskend)
stop.pack()



mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()



text = content.get()
content.set(text)
