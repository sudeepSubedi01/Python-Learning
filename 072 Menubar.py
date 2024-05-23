from tkinter import *

def handleOpen():
  print('Open is clicked')
def handleSave():
  print('Save is clicked')
def handleExit():
  print('Exit is clicked')
def handleCopy():
  print('Copy is clicked')
def handleCut():
  print('Cut is clicked')
def handlePaste():
  print('Paste is clicked')

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=fileMenu)    #creates a dropdown in the menu
fileMenu.add_command(label='Open',command=handleOpen)
fileMenu.add_command(label='Save',command=handleSave)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=handleExit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Copy',command=handleCopy)
editMenu.add_command(label='Cut',command=handleCut)
editMenu.add_command(label='Paste',command=handlePaste)
window.mainloop()