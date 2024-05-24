from tkinter import *

def handleCreateWindow():
  newWindow = Toplevel()    #Toplevel() = new window on top of other windows linked to a buttom window
  # window.destroy()

window = Tk()   #buttom window
Button(window,text='Create new window', command=handleCreateWindow).pack()
window.mainloop()