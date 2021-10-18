from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Salim Karşanbaş").grid(row=1, column=5)
myLabel3 = Label(root, text="                                         ").grid(row=1, column=1)


# myLabel1.grid(row=0, column=0)        # Kodun temizliği açısından bu yöntem daha kullanışlı.
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=1, column=1)


root.mainloop()