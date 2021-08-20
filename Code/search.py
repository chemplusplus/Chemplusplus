from tkinter import ttk
from tkinter import *

import sys

import os

import backend

try:
	import requests
except:
	if sys.platform == "linux":
		os.system('pip3 install requests')
	elif sys.platform == 'windows':
		os.system('pip install requests')

from bs4 import BeautifulSoup

import re

import threading

def search(t):
	if(not t):
		backend.invalid()
		return

	searches = []

	to_return  = []

	query = t.split(" ")
	formatted_query = ""
	for i in range(len(query)):
		formatted_query += query[i]
		formatted_query += "+"
	formatted_query = formatted_query[:len(formatted_query)-1]

	to_search = f'https://chemistry.stackexchange.com/search?q={formatted_query}'

	init_site = requests.get(to_search).text

	soup = BeautifulSoup(init_site, 'html.parser')

	page_1_results = soup.find_all(class_="question-hyperlink")[:3]

	for i in range(len(page_1_results)):
		page_1_results[i] = str(page_1_results[i]).split("href=\"")[1]
		page_1_results[i] = page_1_results[i].split("\"")[0]

	for i in range(len(page_1_results)):
		searches.append(f"https://chemistry.stackexchange.com{page_1_results[i]}")

	for i in range(len(searches)):
		site = requests.get(searches[i])

		soup2 = BeautifulSoup(site.text, "html.parser")

		results = soup2.find_all(class_='s-prose js-post-body')

		answered_time = soup2.find_all(class_='user-action-time')

		authors = soup2.find_all(class_='user-details')

		authors_filtered = []

		answered_time_filtered = []

		for j in range(len(answered_time)):
			if 'edited' not in answered_time[j].text:
				answered_time_filtered.append(answered_time[j].text.lstrip())
				temp = authors[j].text.split()
				authors_filtered.append(temp[0])

		for k in range(len(answered_time_filtered)):
			answered_time_filtered[k] = answered_time_filtered[k].replace('a','A',1).replace('\'','20') + 'by ' + authors_filtered[k] 

		total = ''

		for e in range(len(results)):
			total += '\n' + answered_time_filtered[e] + authors_filtered[e] + '\n--------------------------------------------------'
			total += results[e].text

		total += f"\n\n\n\nSource:\t" + searches[i]

		to_return.append(total)

	search_gui(to_return)

def search_gui(res):
	search_window = Tk()

	search_window.geometry("1200x500")

	search_window.title("Search Results")

	search_window.resizable(False, False)

	search_window.configure(bg = '#373e40')

	scroll = Scrollbar(search_window)

	scroll.pack(side = RIGHT, fill = Y)

	results_title = Label(search_window, text = f'Results for : {_Search_Entry.get()}', font = (backend.GLOBAL_FONT, 24), bg = "#373e40", fg = "#ffffff")

	results_title.pack()

	#35 characters 




	texts = []

	result = Text(search_window, width = 120, height = 25, wrap = WORD, font = (backend.GLOBAL_FONT, 10), yscrollcommand = scroll.set)
	result.insert(END, res[0])
	result.pack()

	scroll.config(command = result.yview)

	global INDEX
	INDEX = 0

	_Forward = ttk.Button(search_window, text = ">", command = lambda:switch(res, result, INDEX+1),width=1)

	_Backward = ttk.Button(search_window, text = "<", command = lambda:switch(res, result, INDEX-1),width=1)

	_Forward.place(x = 40, y = 0)

	_Backward.place(x = 0, y = 0)

def switch(res, txt, index):
	global INDEX

	if index > len(res)-1 or index < 0:
		return None

	if index == INDEX + 1:
		INDEX += 1
	elif index == INDEX - 1:
		INDEX -= 1


	txt.delete('1.0', END)
	txt.insert(END, res[index])
def clear_entry(event):
	global _Search_Entry
	_Search_Entry.delete(0, 'end')
	return None

	
def create_search(t):
	global _Search_Frame, _Search_Entry, _Search_Enter, _Search_Thread

	s = ttk.Style()
	s.configure('TLabelframe',background='#373e40')
	s.configure('TLabelframe.Label',background='#373e40')
	s.configure('TLabelframe.Label',foreground='white')
	_Search_Frame = ttk.LabelFrame(t, text = 'Search', width = 400, height = 80)

	_Search_Frame.place(x = 790, y = 10)

	_Search_Entry = ttk.Entry(_Search_Frame, width = backend.return_size('large'))

	_Search_Entry.insert(0, "Search")

	_Search_Entry.bind("<Button-1>", clear_entry)

	_Search_Entry.place(x = 7, y = 0)

	_Search_Enter = ttk.Button(_Search_Frame, text = "Enter Search", command = lambda:search(_Search_Entry.get()),width=backend.return_size('large'))

	_Search_Enter.place(x = 5, y = 25)
