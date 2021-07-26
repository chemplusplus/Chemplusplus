#for balencing an equation it is a lot like 
#foil in math
#for this reason I need to create something that retruns something


from tkinter import *


# A B2 + C = CB2 + A
# A B2 + 2C = CB2 + A

import string


class equation:
	def __init__(self, r, p):
		self.reactants = r
		self.products = p

	def parse(self):
		self.reactants = self.reactants.replace(" ", "").split("+")
		self.products = self.products.replace(" ",'').split("+")
		rt1 = []
		for i in self.reactants:
			ld = False
			temp = []
			for e in range(len(i)):
				if i[e] in string.ascii_uppercase:
					if ld == False:
						start = i[e]
						ld = True


					elif ld == True:
						temp.append(start+"1")
						start = i[e]


				elif i[e] in string.ascii_lowercase:
					start += i[e]

				elif i[e] in string.digits:
					start += i[e]
					ld = False
					temp.append(start)
					start = ''

			if start != '':
				temp.append(start+"1")
			rt1.append(temp)
		rt2 = []
		for i in self.products:
			ld = False
			temp2 = []
			for e in range(len(i)):
				if i[e] in string.ascii_uppercase:
					if ld == False:
						start = i[e]
						ld = True


					elif ld == True:
						temp2.append(start+"1")
						start = i[e]


				elif i[e] in string.ascii_lowercase:
					start += i[e]

				elif i[e] in string.digits:
					start += i[e]
					ld = False
					temp2.append(start)
					start = ''

			if start != '':
				temp2.append(start+"1")
			rt2.append(temp2)

		self.reactants = rt1
		self.products = rt2
	def balence(self):

		all_elements = []

		for i in self.reactants:
			for e in i:
				for z in range(len(e)):
					if e[z] in string.digits:
						all_elements.append(e[:z])
		for i in self.products:
			for e in i:
				for z in range(len(e)):
					if e[z] in string.digits:
						all_elements.append(e[:z])
		all_elements = list(dict().fromkeys(all_elements))
		print(all_elements)

		rterms = dict()
		pterms = dict()
		for i in self.reactants:
			temp = ""
			for e in i:
				temp += e
			rterms[temp] = []

		for i in self.products:
			temp = ""
			for e in i:
				temp += e
			pterms[temp] = []

		print(rterms, pterms)

		for i in rterms:
			for e in range(len(all_elements)):
				rterms[i].append(0)
		for i in pterms:
			for e in range(len(all_elements)):
				pterms[i].append(0)
		print(rterms, pterms)

		for i in rterms:
			for e in all_elements:
				if e in i:
					

					for z in range(len(i)):


						if i[z:z + len(e) ] == e:

							for q in i[z:z+3]:
								if q in string.digits:
									
									for t in range(len(all_elements)):

										if all_elements[t] == e:

											print(rterms[i])

											rterms[i].insert(t, int(q))
											
											print(rterms[i])
											rterms[i].pop(t+1)
											print(rterms[i],  "\n")
		for i in pterms:
			for e in all_elements:
				if e in i:
					

					for z in range(len(i)):


						if i[z:z + len(e) ] == e:

							for q in i[z:z+3]:
								if q in string.digits:
									
									for t in range(len(all_elements)):

										if all_elements[t] == e:

											print(pterms[i])

											pterms[i].insert(t, int(q))
											
											print(pterms[i])
											pterms[i].pop(t+1)
											print(pterms[i],  "\n")
		#at this point the terms dictionary should look like this 
		#{'N1H3': ['1', '3', 0], 'O2': [0, '2', 0], 'H2O1': ['2', '1', 0]}
		print(rterms, pterms)

		while True:
			for i in range(len(all_elements)):
				rt, pt = 0,0
				for e in rterms:
					rt += rterms[e][i]
				for e in pterms:
					pt += pterms[e][i]
				print(rt, pt)
			break #idk whats happening im tired

def clear_entry(event):
	global _Balence_Entry
	_Balence_Entry.delete(0, 'end')
	return None


def create_balencer(t):

	global _Balence_Frame, _Balence_Entry, _Balence_Enter

	_Balence_Frame = LabelFrame(t, text = 'Equation Balencer', width = 400, height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Balence_Frame.place(x = 10, y = 100)

	_Balence_Entry = Entry(_Balence_Frame,bg = '#ffffff', fg = '#121212', font = ("Montserrat", 10), width = 42)

	_Balence_Entry.insert(0, "Equation")

	_Balence_Entry.bind("<Button-1>", clear_entry)

	_Balence_Enter = Button(_Balence_Frame, text = 'Get Balence', command = lambda:create_window(_Balence_Entry.get()), font = ('Montserrat', 10), width = 40)

	_Balence_Enter.place(x = 5, y = 25)

	_Balence_Entry.place(x = 7, y = 0)



idk = equation("H + O", "H2O")
idk.parse()
print(idk.reactants, idk.products)

idk.balence()
