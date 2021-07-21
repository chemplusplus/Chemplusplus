'''
This is the unit converter file
'''
import backend

from tkinter import *

def conv_calc(en):
	calc_window = Tk()
	calc_window.geometry('400x200')
	calc_window.title('Conversion Calculator')
	calc_window.resizable(False, False)
	calc_window.configure(bg = '#373e40')

	element_entry = Entry(calc_window, width = 10)

	element_entry.insert(0, en)

	grams_entry = Entry(calc_window, width = 10)

	mols_entry = Entry(calc_window, width = 10)

	particles_entry = Entry(calc_window, width = 15)

	element_label = Label(calc_window, text = "Element:", bg = '#373e40', fg = '#ffffff', font = ("Montserrat", 10))

	grams_label = Label(calc_window, text = "Grams", bg = '#373e40', fg = '#ffffff', font = ("Montserrat", 10))

	mols_label = Label(calc_window, text = "Mols", bg = '#373e40', fg = '#ffffff', font = ("Montserrat", 10))

	particles_label = Label(calc_window, text = "Particles", bg = '#373e40', fg = '#ffffff', font = ("Montserrat", 10))

	enter = Button(calc_window, text = "Enter Values", 
		command = lambda:backend.calc_units(particles_entry, mols_entry, grams_entry, element_entry),
		bg = '#373e40', fg = '#ffffff', font = ("Montserrat", 10))

	clear = Button(calc_window, text = "Clear Values", command = lambda:backend.clear_values(particles_entry, mols_entry, grams_entry, element_entry),
			bg = '#373e40', fg = '#ffffff', font = ("Montserrat", 10))

	element_entry.place(x = 165, y = 0)

	element_label.place(x = 85, y = 0)

	grams_entry.place(x = 312, y = 50)

	grams_label.place(x = 315, y = 75)

	mols_entry.place(x = 165, y = 50)

	mols_label.place(x = 165, y = 75)

	particles_entry.place(x = 0,y = 50)

	particles_label.place(x = 0, y = 75)

	enter.place(x = 152, y = 150)

	clear.place(x = 282, y = 150)

def create_converter(t):
	global _Conversion_Frame, _Conversion_Input, _Conversion_Calc_Button

	_Conversion_Frame = LabelFrame(t, text = "Conversion", width = 200, height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Conversion_Frame.place(x = 410, y = 10)

	_Conversion_Input = Entry(_Conversion_Frame, bg = '#ffffff', fg = '#121212', width = 19 ,font = ("Montserrat", 10))

	_Conversion_Input.insert(0, "Element Name")

	_Conversion_Input.place(x = 7, y = 0)

	_Conversion_Calc_Button = Button(_Conversion_Frame, text = 'Convert Units', command = lambda:conv_calc(_Conversion_Input.get()), font = ("Montserrat", 10), width = 17)

	_Conversion_Calc_Button.place(x = 5, y = 25)
