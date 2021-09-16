from tkinter import ttk
from tkinter import *
import backend


def clear_entry(event):
	global _Notation_Entry
	_Notation_Entry.delete(0, 'end')
	return None

def get_Notation():
	global _Notation_Entry

	try:
		number = float(_Notation_Entry.get())
		n = _Notation_Entry.get()

	except:
		backend.invalid()
		return

	if (number < 10 and number > 0) or number == 0:
		return

	exponent = 0
	decimal_places = len(n)-1

	if number > 10:

		while number > 10:

			number /= 10

			exponent += 1
		_Notation_Entry.delete(0, 'end')

		_Notation_Entry.insert(0, str(round(number,decimal_places))+f" * 10 ^ {exponent}")

	elif number < 10:

		while number < 10:

			number *= 10

			exponent -= 1

		_Notation_Entry.delete(0, 'end')

		_Notation_Entry.insert(0, str(round(number,decimal_places)) + f" * 10 ^ {exponent}")

def create_Notation(t):

	global _Notation_Frame, _Notation_Entry,  _Notation_Enter, _Places_Entry

	_Notation_Frame = ttk.LabelFrame(master = t, text = "Scientific Notation", width = 200, height = 80)

	_Notation_Frame.place(x = 410, y = 190)

	_Notation_Entry = ttk.Entry(master = _Notation_Frame, width = backend.return_size('med'))

	_Notation_Entry.insert(0, "Insert Number")

	_Notation_Entry.bind("<Button-1>", clear_entry)

	_Notation_Entry.place(x = 7, y = 0)

	_Notation_Enter = ttk.Button(master = _Notation_Frame, text = "Get Sci Notation",command = get_Notation, width=backend.return_size('med'))

	_Notation_Enter.place(x = 5, y = 25)

