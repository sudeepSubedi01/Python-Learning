from tkinter import *

def handleKeyStroke(event):
  print('Pressed '+event.keysym)
  label.config(text=event.keysym)

window = Tk()
window.bind('<Key>',handleKeyStroke)
label = Label(window,font=('Helvetica',100))
label.pack()
window.mainloop()