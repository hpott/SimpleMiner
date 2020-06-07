from tkinter import *
import os
import subprocess


cmd='.bat '

master = Tk()
master.geometry("250x150")
master.title('SimpleMiner')

e = Entry(master)
e.pack()

e.focus_set()
def taskkill():
	if coin.get()=="ETH":
		subprocess.call("taskkill /f /im EthDcrMiner64.exe", shell=False)
	elif coin.get()=="XMR":
		subprocess.call("taskkill /f /im xmrig.exe", shell=False)
	
		
def taskpause():
	taskkill()
def taskend():
   taskkill()
   quit()

def callback():
   	wal=e.get()
   	subprocess.Popen(coin.get()+cmd+wal)
coin = StringVar(master)
coin.set("XMR")

menu = OptionMenu(master, coin, "XMR", "ETH")
menu.pack()
start = Button(master, text="Start mining", width=10, command=callback)
start.pack()
pause=Button(master, text="Pause Mining", width=10, command=taskpause)
pause.pack()
stop = Button(master, text="Stop Mining", width=10, command=taskend)
stop.pack()




mainloop()
e = Entry(master, width=50)
e.title
e.pack()

text = e.get()



text = content.get()
content.set(text)
