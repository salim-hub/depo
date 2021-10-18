from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# filedialog returns the location

root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\OneDrive\Masaüstü\Tkinter_Course\instagram_icon.ico")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = r"C:\Users\salim\OneDrive\Masaüstü\Tkinter_Course\images", title="Select a File", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()