from tkinter import *

def showValue():
  print('Current value is: ' + selectedValue.get())

window = Tk()
selectedValue=StringVar(window)
selectedValue.set('5')

window.geometry('420x420')
spinBox = Spinbox(window, from_=0,to=10,textvariable=selectedValue)
spinBox.pack()

button = Button(window,text='Show value',command=showValue)
button.pack()

window.mainloop()