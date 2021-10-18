from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course\instagram_icon.ico")

frame = LabelFrame(root, text="This is Frame", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="... or Here!")

b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()