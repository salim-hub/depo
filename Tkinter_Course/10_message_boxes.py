from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course\instagram_icon.ico")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    # messagebox.showinfo("This is my Popup", "Hello Mother Fucker")
    # messagebox.showwarning("This is my Popup", "Hello Mother Fucker")
    # messagebox.showerror("This is my Popup", "Hello Mother Fucker")
    # messagebox.askokcancel("This is my Popup", "Hello Mother Fucker")
    
    response = messagebox.showinfo("This is my Popup", "Hello Mother Fucker")
    Label(root, text=response).pack()
    
    # if response == "yes":
    #     Label(root, text="You Clicked Yes!").pack()
    # else:
    #     Label(root, text="You Clicked No").pack()



Button(root, text="Popup", command=popup).pack()




root.mainloop()