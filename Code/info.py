'''
This is the info file
'''

import backend

from tkinter import *

def info():

	query = _Info_Entry.get()
	if(query in backend.table):
		for i in backend.table:
			if i == query:
				info_window = Tk()
				info_window.geometry("400x400") 
				info_window.title(f"Info {i}")
				info_window.resizable(False, False)
				info_window.configure(bg = '#373e40')
				for e in range(len(backend.table[i])):
					if backend.table[i][e] == '':

						Label(info_window, text = backend.temp2[e]+' = Unknown', bg = '#373e40', fg = '#ffffff').place(x = 0, y = 20*e)
					else:
						Label(info_window, text = backend.temp2[e]+' = '+backend.table[i][e], bg = '#373e40', fg = '#ffffff').place(x = 0, y = 20*e)
	else:
		backend.invalid()


def info_button(x):

	query = x
	for i in backend.table:
		if i == query:
			info_window = Tk()
			info_window.geometry("400x400") 
			info_window.title(f"Info {i}")
			info_window.resizable(False, False)
			for e in range(len(backend.table[i])):
				Label(info_window, text = backend.temp2[e]+' = '+backend.table[i][e]).place(x = 0, y = 20*e)

			break

def clear_entry(event):
	global _Info_Entry
	_Info_Entry.delete(0, 'end')
	return None


def create_info(t):

	global _Info_Entry, _Info_Frame, _Info_Enter


	_Info_Frame = LabelFrame(t, text = 'Element Information', width = 200, height = 80, font = (backend.GLOBAL_FONT, 10), bg = "#373e40", fg = "#ffffff")

	_Info_Frame.place(x = 10, y = 10)

	_Info_Entry = Entry(_Info_Frame,bg = '#ffffff', fg = '#121212', font = (backend.GLOBAL_FONT, 10), width = 22)

	_Info_Entry.insert(0, "Element Name")

	_Info_Entry.bind("<Button-1>", clear_entry)

	_Info_Enter = Button(_Info_Frame, text = 'Get Info', command = info, font = (backend.GLOBAL_FONT, 10), width = 20)

	_Info_Enter.place(x = 5, y = 25)

	_Info_Entry.place(x = 7, y = 0)
