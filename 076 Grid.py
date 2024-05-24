# grid() : geometry manager that organizes widgets in a table like structure in a parent
from tkinter import *

def handleSubmit():
    print('The details are:')
    print('Name: ' + firstNameEntry.get() + ' ' + lastNameEntry.get())
    print('Email: ' + emailNameEntry.get())

window = Tk()
window.geometry('420x420')

titleLabel = Label(window, text='Enter your info:', font=('Arial', 25))     #if grid is used in this line, it will place the grid in in the window but returns zero to the variable and thus get() method will not work properly
titleLabel.grid(row=0, column=0, columnspan=3)

firstNameLabel = Label(window, text='First name:')
firstNameLabel.grid(row=1, column=0)
firstNameEntry = Entry(window)
firstNameEntry.grid(row=1, column=1)

lastNameLabel = Label(window, text='Last name:')
lastNameLabel.grid(row=2, column=0)
lastNameEntry = Entry(window)
lastNameEntry.grid(row=2, column=1)

emailNameLabel = Label(window, text='Email:')
emailNameLabel.grid(row=3, column=0)
emailNameEntry = Entry(window)
emailNameEntry.grid(row=3, column=1)

submitBtn = Button(window, text='Submit', command=handleSubmit)
submitBtn.grid(row=4, column=0, columnspan=2)  # Combines columns 0 and 1, places it in between

window.mainloop()
