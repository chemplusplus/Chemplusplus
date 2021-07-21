'''
This is my chemistry aid for high school students
This was created by Markus Frigaard in 2021
It uses the pubhcem json file for the periodic table



Hexes for colours

bg = 373e40

warnings bg = ffcb77

errors = fe6073

text = fef9ef

black text  = 121212

extra = 17c3b2

'''

import bohr
import info
import math
import string
import menubar
import backend
import converter
from tkinter import *
import tkinter.font as font



root = Tk()

root.configure(bg = '#373e40')

root.geometry("1200x800")

root.title("Chem++")

root.resizable(False, False)




converter.create_converter(root)

menubar.create_menu(root)

info.create_info(root)

bohr.create_bohr(root)


root.mainloop()
