'''
This file is for getting responses from pubchem rest pub api
'''
import json

import urllib3

import urllib.request

import shutil

import os

import sys



def dict_depth(dic, level = 1):
       
    str_dic = str(dic)
    counter = 0
    for i in str_dic:
        if i == "{":
            counter += 1
        if i == "sval":
        	print()
    return(counter)

def get_2d_photo(cid):

	url = f'https://pubchem.ncbi.nlm.nih.gov/image/imagefly.cgi?cid={cid}&width=500&height=500'

	#wget -r -l1 --no-parent -A.gif http://some.website.com/somepage.html

	http = urllib3.PoolManager()

	with http.request('GET', url, preload_content=False) as r, open(f'{cid}.gif', 'wb') as out_file:       
	    shutil.copyfileobj(r, out_file)

	if sys.platform == 'linux':
		if os.getcwd().split("/")[len(os.getcwd().split('/'))-1] != 'photos':
			os.system(f'mv {cid}.gif photos')

	elif sys.platform == 'win32' or sys.platform == 'win64':
		if os.getcwd().split("\\")[len(os.getcwd().split('\\'))-1] != 'photos':
			os.system(f'move {cid}.gif photos')

def get_cid(cname):

	#if there are spaces, they need to be formatted

	for i in range(len(cname)):
		if cname[i] == " ":
			cname = cname[:i] + "%20" + cname[i+1:]


	url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{cname}/JSON"

	the_json = json.loads(urllib.request.urlopen(url).read().decode())

	the_json = the_json["PC_Compounds"][0]['id']['id']['cid']

	


	return the_json

def get_compound(cname):

	#if there are spaces, they need to be formatted

	for i in range(len(cname)):
		if cname[i] == " ":
			cname = cname[:i] + "%20" + cname[i+1:]


	url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{cname}/JSON"

	the_json = json.loads(urllib.request.urlopen(url).read().decode())

	get_info(the_json)

	the_json = the_json["PC_Compounds"][0]['props']

	for_return = []

	for i in the_json:
		if i['urn']['label'] == "SMILES":
			for_return.append(i['value']['sval'])





