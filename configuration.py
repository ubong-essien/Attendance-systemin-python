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

# slide length
slider_text = StringVar()
slider_label = Label(app, text='Slider Length (in meters)', font=('Tmes new roman', 10), pady=20,padx=10)
slider_label.grid(row=0, column=0, sticky=W)
slider_entry = Entry(app, textvariable=slider_text)
slider_entry.grid(row=0, column=1)
# Customer
FOV_text = StringVar()
FOV_label = Label(app, text='Camera FOV (in degree)', font=('Tmes new roman', 10),pady=20, padx=10)
FOV_label.grid(row=1, column=0, sticky=W)
FOV_entry = Entry(app, textvariable=FOV_text)
FOV_entry.grid(row=1, column=1)
# Retailer
OD_text = StringVar()
OD_label = Label(app, text='Object Distance (in meter)', font=('Tmes new roman', 10),pady=20, padx=10)
OD_label.grid(row=2, column=0, sticky=W)
OD_entry = Entry(app, textvariable=OD_text)
OD_entry.grid(row=2, column=1)

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
add_btn = Button(app, text='Save Configuration', width=18, command=add_item)
add_btn.grid(row=3, column=0, pady=20)



app.title('Configuration')
app.geometry('350x500')

# Populate data
#populate_list()

# Start program
app.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''