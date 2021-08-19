'''

This is the backend for my chemistry helper
'''
import string

import re

import os

import sys

import tkinter.messagebox

def add_space(s):
	temp = re.sub('([A-Z])', r' \1', s)
				
	return temp

ELECTRON_CONFIG = dict()
LEVELS = {'1':1, '2':8, '3':8, '4':16, '5':16, '6':16}
S, P, D= 2, 6, 10
LETTERS = {'s':2, 'p':6, 'd':10}

STARTING_DIR = os.getcwd()

import setup

import json 
table = dict()

if sys.platform == "linux":
	temp2 = json.load(open("Assets/ptable.json", 'r'))['Table']['Columns']['Column']

elif sys.platform == 'win32':
	temp2 = json.load(open("Assets/ptable.json", 'r'))['Table']["Columns"]["Column"]
SYMBOLS = []

for i in range(len(temp2)):
	temp2[i] = add_space(temp2[i])
if sys.platform == 'linux':
	temp = json.load(open("Assets/ptable.json", "r"))["Table"]["Row"]
	temp3 = json.load(open("Assets/paions.json", "r"))["Contents"]
	for i in temp3:
		SYMBOLS.append(i)
elif sys.platform == 'win32':
	temp = json.load(open("Assets/ptable.json", "r"))["Table"]["Row"]
	

	
for i in temp:
	table[i['Cell'][2]] = i['Cell']
	ELECTRON_CONFIG[i['Cell'][1]] = i['Cell'][5]
	SYMBOLS.append(table[i['Cell'][2]][1])

class ec:
	def __init__(self, ec):
		temp = ec.split(ec[1])
		self.e = int(temp[1])
		self.level = int(temp[0])
		self.letter = ec[1]

class element:
	def __init__(self, name, ecs, br):
		self.ec = ecs
		self.br = br
		self.name = name



def sub_bohr_config(x):
	for i in ELECTRON_CONFIG:
		if i == x:
			t = ELECTRON_CONFIG[x]
			t = t.split(' ')

			#recursion
			for i in t:
				if i[0] == '[':
					
					for e in (sub_bohr_config(i.split(']')[0][1:])):
						t.append(e)
					r = i[4:]
					t.remove(i)
					t.append(r)

			return t




def config(x):
	name = x
	for i in ELECTRON_CONFIG:
		if i == x:
			x = ELECTRON_CONFIG[i]
			break

	prev = ''
	if x[0] == '[':
		x = x.split(']')
		prev = x[0][1:]
		
		x = x[1:][0]
		for i in ELECTRON_CONFIG:
			if i == prev:
				x+= ' '+ELECTRON_CONFIG[i]
	x = x.split(" ")
	for i in x:
		if i[0] == '(':
			x.remove(i)

	for i in x:
		if i[0] == '[':
			for e in sub_bohr_config(i.split(']')[0][1:]):
				x.append(e)
			t = i[4:]
			x.remove(i)
			x.append(t)
	br = 0
	for i in x:
		if int(i[0]) > br:
			br = int(i[0])

	x = element(name, x, br)
	return x 



def calc_units(pe, me, ge, e):
	temp_pe, temp_me, temp_ge = pe.get(), me.get(), ge.get()
	e = e.get()
	grams_to_mols = 0
	for i in table:
		if i == e:
			grams_to_mols = float(table[i][3])
	if temp_pe != '':
		temp_pe = float(temp_pe)
		me.insert(0, temp_pe/(6.02*10**23))
		ge.insert(0, (temp_pe/(6.02*10**23)*grams_to_mols))
	elif temp_me != '':
		temp_me = float(temp_me)
		pe.insert(0, str(round(temp_me*(6.02),5))+"*10^23")
		ge.insert(0, temp_me/grams_to_mols)

	elif temp_ge != '':
		temp_ge = float(temp_ge)
		me.insert(0, temp_ge/grams_to_mols)
		pe.insert(0, str(round((temp_ge/grams_to_mols)*6.02, 5))+"*10^23")

def clear_values(pe, me, ge, e):
	pe.delete(0, len(pe.get()))
	me.delete(0, len(me.get()))
	ge.delete(0, len(ge.get()))
	#e.delete(0, len(e.get()))

def invalid():
	tkinter.messagebox.showerror(title='Error',message='Invalid Entry')
