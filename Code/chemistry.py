'''
This is my chemistry aid for high school students
This was created by Markus Frigaard in 2021
It uses the pubhcem json file for the periodic table



Hexes for colours

bg = 227c9d

warnings bg = ffcb77

errors = fe6073

text = fef9ef

black text  = 121212

extra = 17c3b2

'''
from tkinter import *

import backend

import math

import string

from PIL import ImageTk, Image



root = Tk()

root.geometry("1200x800")

root.title("Chem++")

root.resizable(False, False)



def info():

	query = _Info_Entry.get()
	for i in backend.table:
		if i == query:
			info_window = Tk()
			info_window.geometry("400x400") 
			info_window.title(f"Info {i}")
			info_window.resizable(False, False)
			for e in range(len(backend.table[i])):
				if backend.table[i][e] == '':

					Label(info_window, text = backend.temp2[e]+' = Unknown').place(x = 0, y = 20*e)
				else:
					Label(info_window, text = backend.temp2[e]+' = '+backend.table[i][e]).place(x = 0, y = 20*e)

			break

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
	for i in backend.table:
		if i == query:
			bohr_window = Tk()
			bohr_window.geometry("600x600")
			bohr_window.title(f"Bohr Diagram {i}")
			bohr_window.resizable(False, False)

			bohr_canvas = Canvas(bohr_window, width = 600, height = 600)
			bohr_canvas.place(x = 0, y = 0)

			for e in backend.table:
				if e == query:
					electrons = backend.config(backend.table[e][1])

			

			print(electrons.name, electrons.ec, electrons.br)

			name_label = Label(bohr_window, bg = 'red',text = f'{backend.table[i][1]}')

			name_label.place(x = 292, y = 292)

			first_circle = bohr_canvas.create_oval(bohr_coords(0,0,25),  fill = 'red')

			_Shell = dict()

			_Electrons = electrons.ec

			for e in range(1, electrons.br+1):
				_Shell[e] = bohr_canvas.create_oval(bohr_coords(0,0,25*(e+1)))

			for e in _Electrons:
				bohr_elec(int(e[2:]), int(e[0]), e[1], bohr_canvas)

			break





_Info_Entry = Entry(root)

_Info_Enter = Button(text = 'Get Info', command = info)

_Info_Enter.place(x = 0, y = 25)

_Info_Entry.place(x = 0, y = 0)
	
_Bohr_Entry = Entry(root)

_Bohr_Enter = Button(root, text = "Get Diagram", command = bohr)

_Bohr_Entry.place(x = 200, y = 0)

_Bohr_Enter.place(x = 200, y = 25)


_Names = []

for i in backend.table:
	_Names.append(i)

_Elements = dict()
def ez_return(x):
	for i in backend.table:
		if i ==x:
			return i



	'''
for i in backend.table:
	
	_Elements[i] = Button(root, text = f'{backend.table[i][0]}\n{backend.table[i][1]}')
c = 1
for i in _Elements:
	for e in _Elements:
		if i == e:

			_Elements[i].configure(command = lambda:info_button(ez_return(i)))
			_Elements[i].grid(row = 1, column = c)
			break
	c += 1
'''




root.mainloop()
