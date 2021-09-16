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
import setup
#setup.install() #comment when compiling to executable
import sys
import os
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
import requests

def callback(url):
    webbrowser.open_new(url)

root = Tk()

s = ttk.Style()
info_x = -1 #ttk on mac os is different on windows and linux
info_y = -1 #this is why we need different spacing to make everything look good
download_x = -1
os_num = -1
authors = "Markus Frigaard and Wayne Zeng"
os = sys.platform #get system platform

if os == "win32" or os == 'win64':
    root.iconbitmap(backend.resource_path("Assets/the_icon.ico")) 
    root.configure(bg = '#373e40')
    app_info = ttk.Label(root,text=f'Chem++ V{backend.version} Windows by {authors}. Visit our website for support:')
    s.configure('Link.TLabel',background='#373e40',foreground='blue')
    s.configure('TLabel',background='#373e40',foreground='white')
    info_x = 655
    info_y = 720
    download_x = 900
    os_num = 2
elif os == 'linux':
	#normally linux should allow .xbm 
	#files as the icon, but it didn't work
	#on linux mint so just gonna use gif
    logo = PhotoImage(file=backend.resource_path('Assets/icon.gif'))
    root.call('wm', 'iconphoto', root._w, logo)
    root.configure(bg = '#373e40')
    app_info = ttk.Label(root,text=f'Chem++ V{backend.version} Linux by {authors}. Visit our website for support:')
    s.configure('Link.TLabel',background='#373e40',foreground='blue')
    s.configure('TLabel',background='#373e40',foreground='white')
    info_x = 555
    info_y = 720
    download_x = 835
    os_num = 0
elif os == 'darwin':
    logo = PhotoImage(file=backend.resource_path('Assets/icon.gif'))
    root.call('wm', 'iconphoto', root._w, logo)
    root.configure(bg = 'white')
    app_info = ttk.Label(root,text=f'Chem++ V{backend.version} Mac_OS by {authors}. Visit our website for support:')
    s.configure('Link.TLabel',foreground='blue')
    info_x = 550
    info_y = 720
    download_x = 845
    os_num = 1
    
app_info.place(x=info_x,y=info_y)

link1 = ttk.Label(root, text="HERE",cursor="hand2",style='Link.TLabel')
link1.place(x=1150,y=info_y)
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

try: #check for updates
    response = requests.get(backend.update_url)
    if(response.json()["tag_name"] != backend.version):
        update_label = ttk.Label(root,text="Update available. Download the latest version:")
        update_label.place(x=download_x,y=info_y+30)
        link_2 = ttk.Label(root,text='HERE',cursor="hand2",style='Link.TLabel')
        download_link = (response.json()["assets"][os_num]["browser_download_url"])
        link_2.bind("<Button-1>", lambda e: callback(download_link))
        link_2.place(x=1150,y=info_y+30) 
    else:
        update_label = ttk.Label(root,text="You are on the latest version")
        update_label.place(x=1000, y=info_y+30)
except:
    update_label = ttk.Label(root,text="Error getting update")
    update_label.place(x=1000, y=info_y+30) 

root.mainloop()
