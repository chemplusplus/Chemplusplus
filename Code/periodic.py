from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import backend
import sys

def create_periodic(t):
    global periodic_button, periodic_label
    periodic_label = ttk.LabelFrame(t, text="View Periodic Table", width=200, height=80)
    periodic_label.place(x=410,y=270)
    periodic_button = ttk.Button(periodic_label,text="View",command=lambda:render_table(),width=backend.return_size('small'))
    periodic_button.place(x=18.5,y=15)

def render_table():
    root = Toplevel()
    root.title("Periodic Table of Elements")
    root.geometry("854x480")

    class Periodic_Table:
        def __init__(self,master):
            if sys.platform == 'darwin':
                self.image = Image.open(backend.resource_path("photos/Periodic.png"))
            elif sys.platform == 'linux':
                self.image = Image.open(backend.resource_path("photos/Periodic.png"))
            elif sys.platform == "win32" or sys.platform == 'win64':
                self.image = Image.open(backend.resource_path("photos\\Periodic.png"))

            self.image_copy = self.image.copy()
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background = Label(master,image = self.background_image)
            self.background.pack(fill=BOTH,expand=YES)
            self.background.bind("<Configure>",self.resize_image)

        def resize_image(self, event):
            new_width = event.width
            new_height = event.height
            self.image = self.image_copy.resize((new_width,new_height),Image.LANCZOS)
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image = self.background_image)

    e = Periodic_Table(root)
    root.mainloop()


