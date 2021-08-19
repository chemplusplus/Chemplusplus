import os, sys

print("""
----------------------
----------------------
----------------------
Checking Dependencies
----------------------
----------------------
----------------------
""")

os.system("pip3 install bs4")
os.system("pip3 install urllib3")
os.system("pip3 install Pillow")

print("Checking fonts")


if sys.platform == 'linux':
	try: 
		os.chdir("Assets/fonts")
	except:
		pass
	for i in os.listdir():
		if i not in os.listdir("/usr/local/share/fonts")
			os.system(f"mv {i} /usr/local/share/fonts")
			print(f"Installed Font {i.split(".")[0]}")
	os.system("fc-cache -f -v")
	print("Cache cleared")
