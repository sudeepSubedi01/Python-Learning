from tkinter import *
import time
from PIL import Image, ImageTk

WIDTH=500
HEIGHT=500
xVelocity = 3
yVelocity = 4
imageHeight= 50 
imageWidth = 50

window = Tk()
photo = ImageTk.PhotoImage(Image.open(r'D:\\Python\\car.png'),height=imageHeight,width=imageWidth)
canvas = Canvas(window,height=HEIGHT,width=WIDTH,bg='aqua')
canvas.pack()
photoInCanvas = canvas.create_image(0,0,image=photo,anchor=NW)

while True:
  coordinates = canvas.coords(photoInCanvas)
  print(coordinates)
  if (coordinates[0] >= 450 or coordinates[0]<0):
    xVelocity = -xVelocity
  if (coordinates[1] >= 450 or coordinates[1]<0):
    yVelocity = -yVelocity
  

  canvas.move(photoInCanvas,xVelocity,yVelocity)
  window.update()
  time.sleep(0.01)
window.mainloop()