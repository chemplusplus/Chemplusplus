'''
This is the unit converter file
'''
import backend
from tkinter import ttk
from tkinter import *

def conv_calc(en):
	calc_window = Tk()
	calc_window.geometry('400x200')
	calc_window.title('Conversion Calculator')
	calc_window.resizable(False, False)
	calc_window.configure(bg = '#373e40')

	element_entry = ttk.Entry(calc_window, width = backend.return_size('med'))

	element_entry.insert(0, en)

	grams_entry = ttk.Entry(calc_window, width = backend.return_size('med'))

	mols_entry = ttk.Entry(calc_window, width = backend.return_size('small'))

	particles_entry = ttk.Entry(calc_window, width = backend.return_size('med'))

	element_label = ttk.Label(calc_window, text = "Element:")

	grams_label = ttk.Label(calc_window, text = "Grams")

	mols_label = ttk.Label(calc_window, text = "Mols")

	particles_label = ttk.Label(calc_window, text = "Particles")

	enter = ttk.Button(calc_window, text = "Enter Values", 
		command = lambda:backend.calc_units(particles_entry, mols_entry, grams_entry, element_entry))

	clear = ttk.Button(calc_window, text = "Clear Values", command = lambda:backend.clear_values(particles_entry, mols_entry, grams_entry, element_entry))

	element_entry.place(x = 165, y = 0)

	element_label.place(x = 85, y = 0)

	grams_entry.place(x = 270, y = 50)

	grams_label.place(x = 270, y = 75)

	mols_entry.place(x = 150, y = 50)

	mols_label.place(x = 150, y = 75)

	particles_entry.place(x = 0,y = 50)

	particles_label.place(x = 0, y = 75)

	enter.place(x = 152, y = 150)

	clear.place(x = 282, y = 150)

def clear_entry(event):
	global _Conversion_Input
	_Conversion_Input.delete(0, 'end')
	return None

def create_converter(t):
	global _Conversion_Frame, _Conversion_Input, _Conversion_Calc_Button

	_Conversion_Frame = ttk.LabelFrame(t, text = "Conversion", width = 200, height = 80)

	_Conversion_Frame.place(x = 410, y = 10)

	_Conversion_Input = ttk.Entry(_Conversion_Frame, width = backend.return_size('med'))

	_Conversion_Input.insert(0, "Element Name")

	_Conversion_Input.bind("<Button-1>", clear_entry)

	_Conversion_Input.place(x = 7, y = 0)

	_Conversion_Calc_Button = ttk.Button(_Conversion_Frame, text = 'Convert Units', command = lambda:conv_calc(_Conversion_Input.get()),width=backend.return_size('med'))

	_Conversion_Calc_Button.place(x = 5, y = 25)
