from tkinter import *
from PIL import Image, ImageTk

def handleW(event):
  print('hellow')
  canvas.move(photo,0,-10)
def handleA(event):
    canvas.move(photo,-10,0)
def handleS(event):
    canvas.move(photo,0,10)
def handleD(event):
    canvas.move(photo,10,0)

window = Tk()
window.bind('<w>', handleW)
window.bind('<s>', handleS)
window.bind('<a>', handleA)
window.bind('<d>', handleD)
photo = ImageTk.PhotoImage(Image.open(r'D:\\Python\\car.png'),height=50,width=50)
canvas = Canvas(window,height=500,width=500,bg='aqua')
canvas.pack()
canvas.create_image(0,0,image = photo,anchor =NW)

window.mainloop()