from tkinter import *
from tkinter import messagebox

def handleClick():
  answer = False
  while answer == False:
    answer = messagebox.askyesno(title='Answer', message='Do you want to do it??')
    if answer == True:
      messagebox.showinfo(title='Answer', message='I want to do it too!!!:)')

window = Tk()
button = Button(window,
                text='Click to reveal',
                command=handleClick)
button.pack()
window.mainloop() 