from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="blue", bg="#ffffff", borderwidth=5)
e.pack()
e.get()
e.insert(0, "Enter Your Name: ")

def myClick():
    helloVar = "Hello " + e.get()
    myLabel = Label(root, text=helloVar)
    myLabel.pack()

myButton = Button(root, text="Enter Your Stock Quote!", command=myClick)
myButton.pack()



root.mainloop()