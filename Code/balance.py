#for balancing an equation it is a lot like 
#foil in math
#for this reason I need to create something that returns something

from tkinter import ttk
from tkinter import *

import sys, os, backend


try:
	from sympy import Matrix, lcm
except:
	if sys.platform == "linux":
		os.system("pip3 install sympy")
	elif sys.platform == 'win32':
		os.system("pip install sympy")


from string import ascii_uppercase as UPPERCASE

from string import ascii_lowercase as LOWERCASE

from string import digits as DIGITS

from backend import SYMBOLS


def get_elements(x):

	elements = []

	for each_term in x:

		for each_element in SYMBOLS:

			if each_term.__contains__(each_element):

				for each_letter in range(len(each_term)):

					if each_term[each_letter:each_letter+len(each_element)] == each_element:

						each_term = each_term[:each_letter] + each_term[each_letter+len(each_element)+1:]

						break



				elements.append(each_element)

	return elements

def reformat(x, e):

	elements = []

	for each_term in x:

		each_term += "  "

		for each_element in e:

			if each_term.__contains__(each_element):

				for each_letter in range(len(each_term)):

					if each_term[each_letter:each_letter+len(each_element)] == each_element:

						if each_term[each_letter+len(each_element)] not in DIGITS:

							each_term = each_term[:each_letter+len(each_element)]+ "1" + each_term[each_letter+len(each_element):]



						

						break

		each_term = each_term[:len(each_term)-2]

		elements.append(each_term)

	return elements

def create_matrices(r, p, e):
	total = len(r) + len(p)
	m = dict()
	for i in range(len(e)):
		m[e[i]]=[0 for e in range(total)]
	num_r, num_p = len(r), len(p)
	r = reformat(r, e)
	p = reformat(p, e)

	for each_term in range(len(r)):

		for each_element in SYMBOLS:

			if r[each_term].__contains__(each_element):

				for each_letter in range(len(r[each_term])):

					if r[each_term][each_letter:each_letter+len(each_element)] == each_element:
	
						m[each_element][each_term] = int(r[each_term][each_letter+len(each_element)])

	for each_term in range(len(p)):

		for each_element in SYMBOLS:

			if p[each_term].__contains__(each_element):

				for each_letter in range(len(p[each_term])):

					if p[each_term][each_letter:each_letter+len(each_element)] == each_element:
	
						m[each_element][each_term+len(r)] = int(p[each_term][each_letter+len(each_element)])*-1

	matr = []

	for i in m:
		matr.append(m[i])

	return matr



def balance(equation):
	try:
		reactants, products = equation.replace(" ", "").split("=")[0].split("+"), equation.replace(" ", "").split("=")[1].split("+")
	except:
		backend.invalid()
		return

	m = create_matrices(reactants, products, get_elements(reactants))

	m = Matrix(m)

	solution=m.nullspace()[0]

	multiple = lcm([val.q for val in solution])

	solution = multiple*solution

	coEffi=solution.tolist()

	output=""

	for i in range(len(reactants)):
		if coEffi[i][0] != 1:
			output+=str(coEffi[i][0])+"("+reactants[i]+")"
		else:
			output+=reactants[i]
		if i<len(reactants)-1:
		   output+=" + "
	output+=" -> "
	for i in range(len(products)):
		if coEffi[i][0] != 1:
			output+=str(coEffi[i+len(reactants)][0])+"("+products[i]+")"
		else:
			output += products[i]
		if i<len(products)-1:
		   output+=" + "
	return output



def create_window(eq):
	global _Balance_Entry
	_Balance_Entry.delete(0, END)
	_Balance_Entry.insert(0, balance(eq))



def clear_entry(event):
	global _Balance_Entry
	_Balance_Entry.delete(0, 'end')
	return None




def create_balancer(t):

	global _Balance_Frame, _Balance_Entry, _balance_Enter

	_Balance_Frame = ttk.LabelFrame(t, text = 'Equation Balancer', width = 400, height = 80)

	_Balance_Frame.place(x = 10, y = 100)

	_Balance_Entry = ttk.Entry(_Balance_Frame, width = backend.return_size('large'))

	_Balance_Entry.insert(0, "Enter Equation")

	_Balance_Entry.bind("<Button-1>", clear_entry)

	_balance_Enter = ttk.Button(_Balance_Frame, text = 'Get Balance', width = backend.return_size('large'),command=lambda:balance(_Balance_Entry.get()))

	_balance_Enter.place(x = 5, y = 25)

	_Balance_Entry.place(x = 7, y = 0)



