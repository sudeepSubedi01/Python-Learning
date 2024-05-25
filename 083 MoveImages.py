from tkinter import *
from PIL import Image, ImageTk

def handleW(event):
  label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def handleS(event):
  label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def handleA(event):
  label.place(x=label.winfo_x()-10,y=label.winfo_y())
def handleD(event):
  label.place(x=label.winfo_x()+10,y=label.winfo_y())

window = Tk()
window.geometry('500x500')
photo = ImageTk.PhotoImage(Image.open(r'D:\\Python\\car.png'),height=50,width=50)
label = Label(window, image=photo)
label.place(x=0,y=0)
window.bind('<w>',handleW)
window.bind('<s>',handleS)
window.bind('<a>',handleA)
window.bind('<d>',handleD)

# Start the Tkinter event loop
window.mainloop()
