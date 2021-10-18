from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course\instagram_icon.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("SECOND WINDOW")
    top.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course\instagram_icon.ico")
    my_img = ImageTk.PhotoImage(Image.open("images/iron_man2.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command = open).pack()


root.mainloop()