from tkinter import *
from tkinter import messagebox

#from db import Database

#db = Database('store.db')


def populate_list():
    # parts_list.delete(0, END)
    # for row in db.fetch():
    #     parts_list.insert(END, row)
    print("populate item");

def add_item():
    # if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
    #     messagebox.showerror('Required Fields', 'Please include all fields')
    #     return
    # db.insert(part_text.get(), customer_text.get(),
    #           retailer_text.get(), price_text.get())
    # parts_list.delete(0, END)
    # parts_list.insert(END, (part_text.get(), customer_text.get(),
    #                         retailer_text.get(), price_text.get()))
    # clear_text()
    # populate_list()
    print("add item");

def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    # db.remove(selected_item[0])
    # clear_text()
    # populate_list()
    print("removeitem")


def update_item():
    # db.update(selected_item[0], part_text.get(), customer_text.get(),
    #           retailer_text.get(), price_text.get())
    # populate_list()
    print("update item")


def clear_text():
    # part_entry.delete(0, END)
    # customer_entry.delete(0, END)
    # retailer_entry.delete(0, END)
    # price_entry.delete(0, END)
    print("clear Text")


# Create window object
app = Tk()

# class Name
Class_name_text = StringVar()
Class_label = Label(app, text='Class Name', font=('Tmes new roman', 10), pady=20,padx=10)
Class_label.grid(row=0, column=0, sticky=W)
Class_entry = Entry(app, textvariable=Class_name_text)
Class_entry.grid(row=0, column=1)
# classdate_text
classdate_text = StringVar()
classdate_label = Label(app, text='Class Date (yyyy-mm-dd)', font=('Tmes new roman', 10),pady=20,padx=10)
classdate_label.grid(row=1, column=0, sticky=W)
classdate_entry = Entry(app, textvariable=classdate_text)
classdate_entry.grid(row=1, column=1)
# Lecturer_text
Lecturer_text = StringVar()
Lecturer_label = Label(app, text='Lecturers Name', font=('Tmes new roman', 10),pady=20,padx=10)
Lecturer_label.grid(row=2, column=0, sticky=W)
Lecturer_entry = Entry(app, textvariable=Lecturer_text)
Lecturer_entry.grid(row=2, column=1)


# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Create Class', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(app, text='Upload Sketch', width=12, command=remove_item)
remove_btn.grid(row=3, column=1)


app.title('Create Attendance')
app.geometry('350x500')

# Populate data
#populate_list()

# Start program
app.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''