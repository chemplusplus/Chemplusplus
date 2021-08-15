from tkinter import *
from PIL import Image, ImageTk
import backend

def create_periodic(t):
    global periodic_button, periodic_label
    periodic_label = LabelFrame(t, text="View Periodic Table", width=200, height=80, font=(
        "Montserrat", 10), bg="#373e40", fg="#ffffff")
    periodic_label.place(x=410,y=270)
    periodic_button = Button(periodic_label,text="View",command=lambda:render_table(),font = ("Montserrat", 10), width = 15)
    periodic_button.place(x=18.5,y=15)

def render_table():
    root = Toplevel()
    root.title("Periodic Table of Elements")
    root.geometry("854x480")

    class Periodic_Table:
        def __init__(self,master):
            self.image = Image.open(".\photos\Periodic.png")
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


