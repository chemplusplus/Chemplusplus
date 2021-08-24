import os
import sys
import backend

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
    os.system("pip3 --disable-pip-version-check install tk bs4 urllib3 Pillow PILLOW sympy")
    if sys.platform == 'darwin':
	    os.system(backend.resource_path('./Certificates.command')) #installs the certificate for pubchem for mac os only


