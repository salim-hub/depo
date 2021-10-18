from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\OneDrive\Masaüstü\Tkinter_Course\instagram_icon.ico")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

# var = IntVar()
# c = Checkbutton(root, text="Check this box", variable=var)

var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect() # deselects it by default
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()