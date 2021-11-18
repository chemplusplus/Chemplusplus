import os
import sys

def install():
    print("""
    ----------------------
    ----------------------
    ----------------------
    Checking Dependencies
    ----------------------
    ----------------------
    ----------------------
    """)
    if sys.platform == 'linux':
	    os.system("sudo apt install python3-pip")
	    os.system("sudo apt-get install python3-tk")
	    os.system("sudo apt-get install python3-pil.imagetk")
    os.system("pip3 --disable-pip-version-check install tk bs4 urllib3 Pillow PILLOW sympy requests")
    if sys.platform == 'darwin':
	    os.system(backend.resource_path('./Certificates.command')) #installs the certificate for pubchem for mac os only


