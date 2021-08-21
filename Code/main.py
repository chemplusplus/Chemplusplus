'''
+-----------------------------------------------------------+
|															|
|	This is my chemistry aid for high school students   	|
|	This was created by Markus Frigaard in 2021  		 	|
|															|
+-----------------------------------------------------------+


Hexes for Colours to be Used:
-----------------------------

Background = 373e40

Warnings Background = ffcb77

Errors = fe6073

Text = fef9ef

Black Text  = 121212

Extra = 17c3b2

'''
import sys
import os

try:
	from PIL import ImageTk, Image
except:
	if sys.platform == 'linux' or sys.platform == 'darwin':
		os.system('pip3 install PILLOW')
		os.system('pip3 install pillow')
	elif sys.platform == 'win32' or sys.platform == 'win64':
		os.system('pip install PILLOW')
		os.system('pip install pillow')	

from PIL import ImageTk, Image

try:
	from sympy import Matrix, lcm
except:
	if sys.platform == "linux" or sys.platform == 'darwin':
		os.system("pip3 install sympy")
	elif sys.platform == 'win32' or sys.platform == 'win64':
		os.system("pip install sympy")

import bohr
import info
import search
import balance
import notation
import structure
import limiting
import converter
import significant
import periodic
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import webbrowser
import backend

def callback(url):
    webbrowser.open_new(url)

root = Tk()

s = ttk.Style()
info_x = -1 #ttk on mac os is different on windows and linux
info_y = -1 #this is why we need different spacing to make everything look good

if sys.platform == "win32" or sys.platform == 'win64':
	#root.iconbitmap("Assets/the_icon.ico") #causes false windows defender detection if uncommented
    root.configure(bg = '#373e40')
    app_info = ttk.Label(root,text='Chem++ V1.0.0 Windows by Markus Frig 2021. Visit our website for support:')
    s.configure('Link.TLabel',background='#373e40',foreground='blue')
    s.configure('TLabel',background='#373e40',foreground='white')
    info_x = 780
    info_y = 720
elif sys.platform == 'linux':
	#normally linux should allow .xbm 
	#files as the icon, but it didn't work
	#on linux mint so just gonna use gif
    logo = PhotoImage(file=backend.resource_path('Assets/icon.gif'))
    root.call('wm', 'iconphoto', root._w, logo)
    root.configure(bg = '#373e40')
    app_info = ttk.Label(root,text='Chem++ V1.0.0 Linux by Markus Frig 2021. Visit our website for support:')
    s.configure('Link.TLabel',background='#373e40',foreground='blue')
    s.configure('TLabel',background='#373e40',foreground='white')
    info_x = 710
    info_y = 720
elif sys.platform == 'darwin':
    logo = PhotoImage(file=backend.resource_path('Assets/icon.gif'))
    root.call('wm', 'iconphoto', root._w, logo)
    root.configure(bg = 'white')
    app_info = ttk.Label(root,text='Chem++ V1.0.0 Mac_OS by Markus Frig 2021. Visit our website for support:')
    s.configure('Link.TLabel',foreground='blue')
    info_x = 700
    info_y = 720
    if sys.platform == 'darwin':
	    os.system(backend.resource_path('./Certificates.command')) #installs the certificate for pubchem for mac os only
    
app_info.place(x=info_x,y=info_y)

link1 = ttk.Label(root, text="HERE",cursor="hand2",style='Link.TLabel')
link1.place(x=1150,y=750)
link1.bind("<Button-1>", lambda e: callback("https://chemplusplus.github.io/"))

root.geometry("1200x800")

root.title("Chem++")

root.resizable(False, False)

limiting.create_limiting(root)
	
balance.create_balancer(root)

converter.create_converter(root)

info.create_info(root)

bohr.create_bohr(root)

search.create_search(root)

structure.create_struct(root)

significant.create_sig(root)

notation.create_Notation(root)

periodic.create_periodic(root)


#this nexte piece of code is copied
#we need to know whether or not its connected because it takes
#away the features of the comopound structures and such
import urllib.request
def connect(host='http://google.com'):
	try:
		urllib.request.urlopen(host) #Python 3.x
		return True
	except:
		return False
# test
if not connect():
	tkinter.messagebox.showwarning('Heads up','You are not connected to the internet. Some features will not work.')
root.mainloop()
