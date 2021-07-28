#for balencing an equation it is a lot like 
#foil in math
#for this reason I need to create something that retruns something


from tkinter import *


# A B2 + C = CB2 + A
# A B2 + 2C = CB2 + A

import string






def clear_entry(event):
	global _Balence_Entry
	_Balence_Entry.delete(0, 'end')
	return None


def create_balencer(t):

	global _Balence_Frame, _Balence_Entry, _Balence_Enter

	_Balence_Frame = LabelFrame(t, text = 'Equation Balencer', width = 400, height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Balence_Frame.place(x = 10, y = 100)

	_Balence_Entry = Entry(_Balence_Frame,bg = '#ffffff', fg = '#121212', font = ("Montserrat", 10), width = 42)

	_Balence_Entry.insert(0, "Under Construction")

	_Balence_Entry.bind("<Button-1>", clear_entry)

	_Balence_Enter = Button(_Balence_Frame, text = 'Get Balence', command = lambda:create_window(_Balence_Entry.get()), font = ('Montserrat', 10), width = 40)

	_Balence_Enter['state'] = 'disabled'

	_Balence_Enter.place(x = 5, y = 25)

	_Balence_Entry.place(x = 7, y = 0)



