from tkinter import *
from tkinter import colorchooser

def handleChoose():
  color = colorchooser.askcolor()
  print(color)
  colorHex = color[1]
  window.config(bg=colorHex)
window = Tk()
window.geometry('420x420')
button = Button(window,
                text='Click to choose',
                command=handleChoose)
button.pack()
window.mainloop()