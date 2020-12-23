#----------------------------------------------------------
# Developer ----- Bryce Martin
# Description --- This file will use tkinter to create a
#                 GUI for the frontend of the app.
#----------------------------------------------------------

# This program will store this information: title, Author, year,
#  and ISBN
#
# User can:
# view all records
# search an entry
# add entry
# update entry
# Delete
# Close
#----------------------------------------------------------

from tkinter import *
import backend

#this function will retrieve data (tuple) from the database
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    #get the stringvar in the widget and apply the get method
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END,row)

def insert_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()))
#opens a window ready for customization
window = Tk()

#creating the labels first
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

#add the entries
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0,column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0,column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1,column=1)

ISBN_text = StringVar()
entry4 = Entry(window, textvariable=ISBN_text)
entry4.grid(row=1,column=3)

#adding the list box
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

#adding scrollbar
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)

#adding the buttons - NEED TO ADD COMMAND PARAMATER for the functions
btn1 = Button(window, text= "view all", width=12, command=view_command)
btn1.grid(row=2,column=3)

btn2 = Button(window, text= "Search Entry", width=12, command=search_command)
btn2.grid(row=3,column=3)

btn3 = Button(window, text= "Add Entry", width=12, command= insert_command)
btn3.grid(row=4,column=3)

btn4 = Button(window, text= "Update", width=12)
btn4.grid(row=5,column=3)

btn5 = Button(window, text= "Delete", width=12)
btn5.grid(row=6,column=3)

btn6 = Button(window, text= "Close", width=12)
btn6.grid(row=7,column=3)


#wraps up all widgets
window.mainloop()
