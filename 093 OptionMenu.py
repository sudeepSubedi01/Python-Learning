from tkinter import *

def showSelection():
  print('selected item: '+ selectedOption.get())

window = Tk()
options =['Rice','Dal','Chicken','Burger']
selectedOption = StringVar(window)
selectedOption.set(options[0])

optionWidget = OptionMenu(window,selectedOption, *options)
optionWidget.pack()

button = Button(window,text='Show selection', command= showSelection)
button.pack()

window.mainloop()