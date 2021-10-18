from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course\instagram_icon.ico")


my_img = ImageTk.PhotoImage(Image.open("iron_man.jpg"))
my_label = Label(image=my_img)
my_label.pack()








button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()