'''
This is the bohrmenu
'''

from tkinter import *

import math

import backend

import sys


def bohr_coords(x, y, w):
	nx, ny = 300 + x, 300 + -1*y
	to_return = [nx+w, ny+w, nx-w, ny-w]
	return to_return 


def bohr_elec(n, r, x,canv): #x refers to the place where they will be printed
	m30 = math.cos(math.radians(30))
	m45= math.cos(math.radians(45))
	m60 = math.cos(math.radians(60))

	spos = [(-5, 25*(r+1)), (5,(25*(r+1)))]

	ppos = [(25*(r+1), 5) , (25*(r+1), -5), 
	(5, -25*(r+1)), (-5, -25*(r+1)), 
	(-25*(r+1), -5), (-25*(r+1), 5)]

	dpos = [
	(m45 *25*(r+1)+10, m45*25*(r+1)-10), 
	(m45*25*(r+1), m45*25*(r+1)), 
	(m45*25*(r+1)-10, m45*25*(r+1)+10),
	(m45*25*(r+1)+5,m45*-25*(r+1)+5), 
	(m45*25*(r+1)-5, m45*-25*(r+1)-5), 

	(m45 *-25*(r+1)+10, m45*-25*(r+1)-10), 
	(m45*-25*(r+1), m45*-25*(r+1)), 
	(m45*-25*(r+1)-10, m45*-25*(r+1)+10),
	(m45*-25*(r+1)+5,m45*25*(r+1)+5), 
	(m45*-25*(r+1)-5, m45*25*(r+1)-5)]#this is for the placement of electrons on the bohr diagram

	fpos = [
	(m60 *25*(r+1)-5, m30*25*(r+1)+3), 
	(m60*25*(r+1)-20, m30*25*(r+1)+10), 
	
	(m30*25*(r+1)+3, m60*25*(r+1)-5),
	(m30*25*(r+1)+10,m60*25*(r+1)-20), 
	
	(m30*25*(r+1)+3, m60*-25*(r+1)+5), 
	(m30*25*(r+1)+10, m60*-25*(r+1)+20), 
	
	(m60*25*(r+1)-5, m30*-25*(r+1)-3), 
	(m60*25*(r+1)-20, m30*-25*(r+1)-10),
	
	(m60*-25*(r+1)+5,m30*-25*(r+1)-3), 
	(m60*-25*(r+1)+20, m30*-25*(r+1)-10), 
	
	(m30*-25*(r+1)-3, m60*-25*(r+1)+5), 
	(m30*-25*(r+1)-10, m60*-25*(r+1)+20),
	
	(m30*-25*(r+1)-5, m60*25*(r+1)-5),

	(m60*-25*(r+1)+5, m30*25*(r+1)+5)]


	if x == 's':
		for i in range(n):
			canv.create_oval(bohr_coords(spos[i][0], spos[i][1], 5), fill = 'yellow')

	elif x == 'p':
		for i in range(n):
			canv.create_oval(bohr_coords(ppos[i][0], ppos[i][1], 5), fill = 'pink')

	elif x =='d':
		for i in range(n):
			canv.create_oval(bohr_coords(dpos[i][0], dpos[i][1], 5), fill = 'cyan')

	elif x == 'f':
		for i in range(n):
			canv.create_oval(bohr_coords(fpos[i][0], fpos[i][1], 5), fill = 'green')

def bohr():

	query = _Bohr_Entry.get()
	if query in backend.table:
		for i in backend.table:
			if i == query:
				bohr_window = Tk()
				bohr_window.geometry("600x600")
				bohr_window.title(f"Bohr Diagram {i}")
				bohr_window.resizable(False, False)


				bohr_canvas = Canvas(bohr_window, width = 600, height = 600, bg = '#373e40')
				bohr_canvas.place(x = -1, y = -1)

				for e in backend.table:
					if e == query:
						electrons = backend.config(backend.table[e][1])

				bohr_info = Label(bohr_window, text = f'Electrons = {backend.table[query][0]}\nCharge = {backend.table[query][10]}',
					font = (backend.GLOBAL_FONT, 10), bg = "#373e40", fg = "#ffffff")
				bohr_info.place(x = 5, y = 5)

				name_label = Label(bohr_window, bg = 'red',text = f'{backend.table[i][1]}')

				name_label.place(x = 290, y = 290)

				first_circle = bohr_canvas.create_oval(bohr_coords(0,0,25),  fill = 'red')

				_Shell = dict()

				_Electrons = electrons.ec

				for e in range(1, electrons.br+1):
					_Shell[e] = bohr_canvas.create_oval(bohr_coords(0,0,25*(e+1)))

				for e in _Electrons:
					bohr_elec(int(e[2:]), int(e[0]), e[1], bohr_canvas)
	else:
		backend.invalid()
				

def clear_entry(event):
	global _Bohr_Entry
	_Bohr_Entry.delete(0, 'end')
	return None


def create_bohr(t):
	global _Diagram_Frame, _Bohr_Entry, _Bohr_Enter

	_Diagram_Frame = LabelFrame(t, text = "Bohr Diagram", width = 200, height = 80, font = (backend.GLOBAL_FONT, 10), bg = "#373e40", fg = "#ffffff")

	_Diagram_Frame.place(x = 210, y = 10)
		
	_Bohr_Entry = Entry(_Diagram_Frame,bg = '#ffffff', fg = '#121212', width = 22 ,font = (backend.GLOBAL_FONT, 10))

	_Bohr_Entry.insert(0, "Element Name")

	_Bohr_Entry.bind("<Button-1>", clear_entry)

	_Bohr_Enter = Button(_Diagram_Frame, text = "Get Diagram", width = 20,command = bohr, font = (backend.GLOBAL_FONT, 10))

	_Bohr_Entry.place(x = 7, y =0)

	_Bohr_Enter.place(x = 5, y = 25)
