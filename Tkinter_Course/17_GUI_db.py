from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Learn to Code")
root.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course")
root.geometry("400x600")

# Databases

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# CREATE CURSOR
c = conn.cursor()

# Create table
# '''
# c.execute("""CREATE TABLE addresses (
# 		first_name text,
# 		last_name text,
# 		address text,
# 		city text,
# 		state text,
# 		zipcode integer
# 		)""")
# '''


# Create Submit Function For Database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # CREATE CURSOR
    c = conn.cursor()

    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
        [
            f_name.get(),
            l_name.get(),
            address.get(),
            city.get(),
            state.get(),
            zipcode.get(),
        ])

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    

# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # CREATE CURSOR
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    # Loop Through Results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


# CREATE TEXT BOXES
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)


# CREATE TEXT BOX LABELS
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)


# CREATE SUBMIT BUTTON
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# CREATE a QUERY BUTTON
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()