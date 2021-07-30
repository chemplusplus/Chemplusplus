from tkinter import *


def clear_entry(event):
	global _Notation_Entry
	_Notation_Entry.delete(0, 'end')
	return None

def get_Notation():
	global _Notation_Entry

	try:
		number = float(_Notation_Entry.get())
		string_version = _Notation_Entry.get()

	except:

		return 

	if (number < 10 and number > 0) or number == 0:
		return 

	exponent = 0

	if number > 10:

		while number > 10:

			number /= 10

			exponent += 1
		_Notation_Entry.delete(0, 'end')

		_Notation_Entry.insert(0, str(round(number, 2))+f" * 10 ^ {exponent}")

	elif number < 10:

		while number < 10:

			number *= 10

			exponent -= 1

		_Notation_Entry.delete(0, 'end')

		_Notation_Entry.insert(0, str(round(number, 2)) + f" * 10 ^ {exponent}")





def create_Notation(t):

	global _Notation_Frame, _Notation_Entry,  _Notation_Enter, _Places_Entry

	_Notation_Frame = LabelFrame(master = t, text = "Scientific Notation", width = 200, 
						height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Notation_Frame.place(x = 410, y = 190)

	_Notation_Entry = Entry(master = _Notation_Frame, bg = '#ffffff', fg = '#121212', width = 19 ,font = ("Montserrat", 10))

	_Notation_Entry.insert(0, "Insert Number")

	_Notation_Entry.bind("<Button-1>", clear_entry)

	_Notation_Entry.place(x = 7, y = 0)

	_Notation_Enter = Button(master = _Notation_Frame, text = "Get Sci Notation",command = get_Notation,
		width = 17, font = ("Montserrat", 10))

	_Notation_Enter.place(x = 5, y = 25)

