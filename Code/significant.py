from tkinter import *
import backend

def clear_first(event):
	global _Sig_Entry
	_Sig_Entry.delete(0, 'end')
	return None


def clear_second(event):
	global _Places_Entry
	_Places_Entry.delete(0, 'end')
	return None

def get_sig():
	global _Places_Entry, _Sig_Entry
	try:
		number = float(_Sig_Entry.get())
		places = int(_Places_Entry.get())

	except:
		backend.invalid()
		return

	string_version = _Sig_Entry.get()

	_Sig_Entry.delete(0, 'end')
	_Places_Entry.delete(0, 'end')

	if len(string_version.split(".")) == 1:
		if len(string_version) <= places:

			_Sig_Entry.insert(0, string_version)

		elif len(string_version) > places:

			zeros = len(string_version) - places

			
			if int(string_version[places]) < 5:
				_Sig_Entry.insert(0, string_version[:places] + "0"*zeros)
			else:
				_Sig_Entry.insert(0, string_version[:places-1] + str(int(string_version[places-1])+1) + "0"*zeros)
	elif len(string_version.split(".")) == 2:
		string_version = string_version.split(".")

		if len(string_version[0]) <= places:
			places -= len(string_version[0])

			if len(string_version[1]) <= places:

				_Sig_Entry.insert(0, string_version[0]+"."+string_version[1])

			elif len(string_version[1]) > places:

				if int(string_version[1][places]) < 5:

					_Sig_Entry.insert(0, string_version[0]+"."+string_version[1][:places])

				else:

					_Sig_Entry.insert(0, string_version[0]+"."+string_version[1][:places-1]+str(int(string_version[1][places-1])+1))

		elif len(string_version[0]) > places:

			zeros = len(string_version[0]) - places

			if int(string_version[0][places]) < 5:

				_Sig_Entry.insert(0, string_version[0][:places]+ "0"*zeros)

			else:

				_Sig_Entry.insert(0, string_version[0][:places-1]+str(int(string_version[0][places-1])+1) +"0"*zeros)








def create_sig(t):

	global _Sig_Frame, _Sig_Entry,  _Sig_Enter, _Places_Entry

	_Sig_Frame = LabelFrame(master = t, text = "Significant Figures", width = 400, 
						height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Sig_Frame.place(x = 10, y = 190)

	_Sig_Entry = Entry(master = _Sig_Frame, bg = '#ffffff', fg = '#121212', width = 30 ,font = ("Montserrat", 10))

	_Sig_Entry.insert(0, "Insert Number")

	_Sig_Entry.bind("<Button-1>", clear_first)

	_Sig_Entry.place(x = 7, y = 0)

	_Sig_Enter = Button(master = _Sig_Frame, text = "Get Result",command = get_sig,
		width = 40, font = ("Montserrat", 10))

	_Sig_Enter.place(x = 5, y = 25)

	_Places_Entry = Entry(master = _Sig_Frame, bg = '#ffffff', fg = '#121212', width = 10 ,font = ("Montserrat", 10))

	_Places_Entry.insert(0, "Places")

	_Places_Entry.bind("<Button-1>", clear_second)

	_Places_Entry.place(x = 290, y = 0)



