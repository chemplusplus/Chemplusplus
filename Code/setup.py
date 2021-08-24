import os

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


