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

def update():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # CREATE CURSOR
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
            'first' : f_name_editor.get(),
            'last' : l_name_editor.get(),
            'address' : address_editor.get(),
            'city' : city_editor.get(),
            'state' : state_editor.get(),
            'zipcode' : zipcode_editor.get(),

            'oid' : record_id
        }
    )


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    editor.destroy()


# Create Edit Function to Update a Record
def edit():
    global editor
    editor = Tk()
    editor.title("Update A Record")
    editor.iconbitmap(r"C:\Users\salim\PycharmProjects\Tkinter_Course")
    editor.geometry("400x200")

    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # CREATE CURSOR
    c = conn.cursor()

    record_id = delete_box.get()

    # Query the Database
    c.execute("SELECT * FROM addresses WHERE oid= " + record_id)
    records = c.fetchall()
    

    # Create Global Variables for Text Box Names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # CREATE TEXT BOXES
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)


    # CREATE TEXT BOX LABELS
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10,0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Create a Save Button To Save Edited Record
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Loop Through Results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

# CREATE FUNCTION TO DELETE A RECORD
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # CREATE CURSOR
    c = conn.cursor()

    # Delete A Record
    c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


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
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


# CREATE TEXT BOXES
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

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

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


# CREATE TEXT BOX LABELS
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))

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

delete_label = Label(root, text="Select ID")
delete_label.grid(row=9, column=0, pady=5)


# CREATE SUBMIT BUTTON
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=4, pady=10, padx=10, ipadx=109)

# CREATE a QUERY BUTTON
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=139)

# Create an Update Button
update_btn = Button(root, text="Edit Record", command=edit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()