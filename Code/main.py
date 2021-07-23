'''
+-----------------------------------------------------------+
|															                              |
|	This is my chemistry aid for high school students   	    |
|	This was created by Markus Frigaard in 2021  		 	        |
|														                              	|
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
import bohr
import info
import math
import string
import search
import menubar
import backend
import threading
import converter
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image



root = Tk()

root.configure(bg = '#373e40')

root.geometry("1200x800")

root.title("Chem++")

root.resizable(False, False)

if sys.platform == "windows":
	root.iconbitmap("assets\\the_icon.ico")

elif sys.platform == 'linux':
	#normally linux should allow .xbm 
	#files as the icon, but it didn't work
	#on linux mint so just gonna use gif
    logo = PhotoImage(file='assets/icon.gif')
    root.call('wm', 'iconphoto', root._w, logo)




converter.create_converter(root)

menubar.create_menu(root)

info.create_info(root)

bohr.create_bohr(root)

search.create_search(root)


root.mainloop()
