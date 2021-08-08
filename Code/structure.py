'''
This is the structure grabber file
'''

from tkinter import *

import time

import backend

import pubchem

import os

def clear_entry(event):
	global _Struct_Entry
	_Struct_Entry.delete(0, 'end')
	return None


def create_struct(t):
	global _Struct_Frame, _Struct_Entry, _Struct_Enter

	_Struct_Frame = LabelFrame(t, text = 'Compound Diagram', width = 200, height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Struct_Frame.place(x = 410, y = 100)

	_Struct_Entry = Entry(_Struct_Frame,bg = '#ffffff', fg = '#121212', font = ("Montserrat", 10), width = 19)

	_Struct_Entry.insert(0, "Compound Name")

	_Struct_Entry.bind("<Button-1>", clear_entry)

	_Struct_Enter = Button(_Struct_Frame, text = 'Get Struct', command = lambda:create_window(), font = ('Montserrat', 10), width = 17)

	_Struct_Enter.place(x = 5, y = 25)

	_Struct_Entry.place(x = 7, y = 0)

def create_window():

	global _Struct_Entry

	x = _Struct_Entry.get()

	try:
		cid = pubchem.get_cid(x)
	except:
		backend.invalid()
		return

	_struct_Window = Tk()

	_struct_Window.geometry('500x500')

	_struct_Window.title(f'Diagram of {x}')

	_struct_Window.resizable(False, False)
	
	global my_image, _diagram


	pubchem.get_2d_photo(cid)


	if os.getcwd().split("/")[len(os.getcwd().split('/'))-1] != 'photos':
	 	os.chdir('photos')



	if f'{cid}.gif' not in os.listdir():
	 	time.sleep(5)


	my_image = PhotoImage(master = _struct_Window, file = f'{cid}.gif')

	_diagram = Label(master =_struct_Window, image = my_image)

	_diagram.pack()


