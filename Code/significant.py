from tkinter import ttk
from tkinter import *
import backend
import sys

def clear_first(event):
	global _Sig_Entry
	_Sig_Entry.delete(0, 'end')
	return None


def clear_second(event):
	global _Places_Entry
	_Places_Entry.delete(0, 'end')
	return None

def get_sf():
	try:
		n = float(_Sig_Entry.get())
	except ValueError:
		backend.invalid()
		return
	value = _Sig_Entry.get()
	_Places_Entry.delete(0, 'end')
	leading = True
	decimal = False
	zeroCount = 0
	sigFig = 0
	for i in range(0,len(value)):
		if leading and value[i] != '0' and value[i] != '.':
			leading=False
			sigFig+=1
		elif not leading and value[i] != '0' and value[i] != '.':
			sigFig+=1
			if zeroCount > 0:
				sigFig+=zeroCount
				zeroCount=0
		elif not leading and value[i] == '0' and not decimal:
			zeroCount+=1
		elif value[i] == '.': #decimal found
			decimal = True
			sigFig+=zeroCount
		elif decimal and value[i] == '0' and not leading:
			sigFig+=1
	_Places_Entry.insert(0,sigFig)

def get_sig():
	global _Places_Entry, _Sig_Entry
	try:
		number = float(_Sig_Entry.get())
		places = int(_Places_Entry.get())

	except ValueError:
		backend.invalid()
		return
	
	string_version = _Sig_Entry.get()

	_Sig_Entry.delete(0, 'end')

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

	_Sig_Frame = ttk.LabelFrame(master = t, text = "Significant Figures", width = 400, height = 80)

	_Sig_Frame.place(x = 10, y = 190)

	_Sig_Entry = ttk.Entry(master = _Sig_Frame, width = backend.return_size('large')-5)

	_Sig_Entry.insert(0, "Insert Number")

	_Sig_Entry.bind("<Button-1>", clear_first)

	_Sig_Entry.place(x = 7, y = 0)

	_Sig_Enter = ttk.Button(master = _Sig_Frame, text = "Get Number",command = get_sig, width = backend.return_size('med'))

	_sf_Enter = ttk.Button(master = _Sig_Frame, text = "Get S.F",command = get_sf, width = backend.return_size('med'))

	_Sig_Enter.place(x = 5, y = 25)

	if sys.platform == 'darwin':
		_sf_Enter.place(x=155,y=25)
	else:
		_sf_Enter.place(x=140,y=25)

	_Places_Entry = ttk.Entry(master = _Sig_Frame, width=backend.return_size('small'))

	_Places_Entry.insert(0, "Places")

	_Places_Entry.bind("<Button-1>", clear_second)

	_Places_Entry.place(x = 290, y = 0)



