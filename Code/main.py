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
import os
import sys
import bohr
import info
import math
import string
import search
import backend
import balence
import notation
import structure
import threading
import converter
import significant
import periodic
from tkinter import *
import tkinter.font as font

try:
	from PIL import ImageTk, Image
except:
	if sys.platform == 'linux':
		os.system('pip3 install PILLOW')
		os.system('pip3 install pillow')
	elif sys.platform == 'win32' or sys.platform == 'win64':
		os.system('pip install PILLOW')
		os.system('pip install pillow')

from PIL import ImageTk, Image


root = Tk()

root.configure(bg = '#373e40')

root.geometry("1200x800")

root.title("Chem++")

root.resizable(False, False)

if sys.platform == "win32":
	root.iconbitmap("Assets/the_icon.ico")

elif sys.platform == 'linux':
	#normally linux should allow .xbm 
	#files as the icon, but it didn't work
	#on linux mint so just gonna use gif
    logo = PhotoImage(file='Assets/icon.gif')
    root.call('wm', 'iconphoto', root._w, logo)


#balence.create_balencer(root)

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
print( 'connected' if connect() else 'no internet!' )

root.mainloop()
