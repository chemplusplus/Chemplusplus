#for balencing an equation it is a lot like 
#foil in math
#for this reason I need to create something that retruns something


from tkinter import *


# A B2 + C = CB2 + A
# A B2 + 2C = CB2 + A

from string import ascii_uppercase as UPPERCASE

from string import ascii_lowercase as LOWERCASE

from string import digits as DIGITS

def get_names(x):

	for each_string in range(len(x)):

		term = x[each_string] #this makes it easier to read

		final_name = "" #this is what will replace each term in the reactants
						#for example H2O will now give us H2O1 so that we may identify 

		looking = False #this will tell us whether or not we are trying to find the end to the chemical

		current = "" #this will store the characters that have been collected so far

		for each_letter in range(len(term)):



			if term[each_letter] in UPPERCASE:

				#there are now two options 

				if looking == False:

					looking = True

					current = term[each_letter]

				elif looking:

					if term[each_letter-1] not in DIGITS: #this makes sure that no element is left without a number of atoms

						current += "1"

					final_name += current

					current = term[each_letter]

			elif term[each_letter] in LOWERCASE:

				current += term[each_letter]

			elif term[each_letter] in DIGITS:

				current += term[each_letter]

				final_name += current

				looking = False


		if term[each_letter] not in DIGITS: #this makes sure that no element is left without a number of atoms

			current += "1"

		final_name += current

		x[each_string] = final_name

	return x
def get_elements(x):

	#this function aims to find all the possible elements in a string

	elements_included = []

	for each_term in x:

		for each_letter in range(len(each_term)):

			if each_term[each_letter] in UPPERCASE:

				if each_letter != len(each_term) -1: #this is to stop errors

					if each_term[each_letter] in LOWERCASE:

						elements_included.append(each_term[each_letter:each_letter+2])
					else:
						elements_included.append(each_term[each_letter])

	return list(dict.fromkeys(elements_included))

def create_matrix(x, n): #this creates a matrix of values from reactants or products
	#x is to be a string of reactants or products
	#n is to be a list of all the elements in a reaction
	
	for each_term in range(len(x)):

		term_name = x[each_term]

		temporary_dict = {term_name : []}

		for each in range(len(n)):

			temporary_dict[term_name].append(0)

		for each in range(len(n)):

			for each_letter in range(len(term_name)):

				if each_letter != len(term_name) - 1:

					if n[each] == term_name[each_letter:each_letter+len(n[each])]:

						temporary_dict[term_name][each] = int(term_name[each_letter + len(n[each])])




		x[each_term] = temporary_dict

	return x


def get_equation(equation):

	#in a chemical equation it is like a + b = c + d

	equation = equation.replace(" ", "").split("=") # by doing this it makes sure we get the operators
	#the .split is simply giving us the reactants on the left side of the equality sign
	#and the product son the right side
	reactants, products =  get_names(equation[0].split("+")), get_names(equation[1].split("+"))

	elements_included = get_elements(reactants) #this only needs to be done on one of the two as there cannot be missing elements
	#just to be sure however

	if get_elements(reactants) != get_elements(products):

		return None

	reactants, products = create_matrix(reactants, elements_included), create_matrix(products, elements_included)







	return_dict = {"reactants" : reactants, 
	'products' : products, 
	'elements_included' : elements_included}

	return return_dict

idx = get_equation("H + O = H2O")
for i in idx:
	print(i, 2*"\t", idx[i])


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



