'''
This is the file for limiting reagents
'''

from tkinter import *

from backend import SYMBOLS

from backend import table

from string import digits as DIGITS

def get_elements(x):

	elements = []

	x += "***"


	for each_element in SYMBOLS:

		if x.__contains__(each_element):


			for each_letter in range(len(x)):


				if x[each_letter:each_letter+len(each_element)] == each_element and x[each_letter+len(each_element)] in list(DIGITS):


					x = x[:each_letter] + x[each_letter+len(each_element)+1:]

					elements.append(each_element)

					break



	
	print(elements)
	return elements

def clear_entry_equation(event):
	global _Equation_Entry
	_Equation_Entry.delete(0, 'end')
	return None

def clear_entry_mass(event):
	global _Mass_Entry
	_Mass_Entry.delete(0, 'end')
	return None

def convert(x):
	r = dict()
	for i in x:
		r[i] = [get_elements(i)]
		if i[0] in DIGITS:
			r[i].append(int(i[0]))
		else:
			r[i].append(1)
		r[i].append([])
		for e in table:
			if table[e][1] in r[i][0]:
				
				r[i][2].append(float(table[e][3]))
		total = 0
		for e in r[i][2]:
			total += e
		r[i][2] = total
	return r

def limit(x, m):
	global DIGITS

	reactants = x.replace(" ", "").split("=")[0].split("+")
	products = x.replace(" ", "").split("=")[1].split("+")

	reactants = convert(reactants)
	products = convert(products)

	


	print(reactants, products)


def create_limiting(t):
	#this is just repetetive stuff from all the other files to create the widgets on the main page

	global _Limiting_Entry, _Limiting_Frame, _Limiting_Enter, _Equation_Entry, _Mass_Entry


	_Limiting_Frame = LabelFrame(t, text = 'Limiting Reagent', width = 400, height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Limiting_Frame.place(x = 10, y = 270)

	_Equation_Entry = Entry(_Limiting_Frame,bg = '#ffffff', fg = '#121212', font = ("Montserrat", 10), width = 30)

	_Equation_Entry.insert(0, "Balenced Equation")

	_Equation_Entry.bind("<Button-1>", clear_entry_equation)

	_Mass_Entry = Entry(_Limiting_Frame,bg = '#ffffff', fg = '#121212', font = ("Montserrat", 10), width = 10)

	_Mass_Entry.insert(0, "Insert Mass")

	_Mass_Entry.bind("<Button-1>", clear_entry_mass)

	_Limiting_Enter = Button(_Limiting_Frame, text = 'Get Limiting Reagent', command = lambda:limit(_Equation_Entry.get(), _Mass_Entry.get()), font = ('Montserrat', 10), width = 40)

	_Limiting_Enter.place(x = 5, y = 25)

	_Equation_Entry.place(x = 7, y = 0)

	_Mass_Entry.place(x = 290, y = 0)