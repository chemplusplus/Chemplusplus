'''
This is the structure grabber file
'''
from tkinter import ttk
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

	_Struct_Frame = ttk.LabelFrame(t, text = 'Compound Diagram', width = 200, height = 80)

	_Struct_Frame.place(x = 410, y = 100)

	_Struct_Entry = ttk.Entry(_Struct_Frame, width = backend.return_size('med'))

	_Struct_Entry.insert(0, "Compound Name")

	_Struct_Entry.bind("<Button-1>", clear_entry)

	_Struct_Enter = ttk.Button(_Struct_Frame, text = 'Get Struct', command = lambda:create_window(), width = backend.return_size('med'))

	_Struct_Enter.place(x = 5, y = 25)

	_Struct_Entry.place(x = 7, y = 0)

def create_window():
	global _Struct_Entry

	x = _Struct_Entry.get().capitalize()

	try:
		cid = pubchem.get_cid(x)

	except:
		_Struct_Entry.delete(0, END)
		
		_Struct_Error = Tk()

		_Struct_Error.resizable(False, False)

		_Struct_Error.title("Error")

		_Struct_Error.geometry("300x100")

		_Struct_Error.config(bg = '#373e40')

		Error_Message = "We could not find the\n compound you were looking for,\n try spelling out the \nfull name"

		_Error_Label = Label(master = _Struct_Error, text = Error_Message, bg = "#373e40", fg = "#ffffff",font = (backend.GLOBAL_FONT, 10))

		_Error_Label.pack()

		return

	global my_image, _diagram

	pubchem.get_2d_photo(cid)

	if os.getcwd().split("/")[len(os.getcwd().split('/'))-1] != backend.resource_path('photos'):
	 	os.chdir(backend.resource_path('photos'))

	if f'{cid}.gif' not in os.listdir():
	 	time.sleep(5)

	_struct_Window = Tk()

	_struct_Window.geometry('500x500')

	_struct_Window.title(f'Diagram of {x}')

	_struct_Window.resizable(False, False)

	my_image = PhotoImage(master = _struct_Window, file = f'{cid}.gif')

	_diagram = Label(master =_struct_Window, image = my_image)

	_diagram.pack()




