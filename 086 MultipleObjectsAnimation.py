from tkinter import *
import time

HEIGHT = 500
WIDTH = 500

class Ball:
  def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
    self.canvas = canvas
    self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity
  def move(self):
    coordinates = self.canvas.coords(self.image)
    # print(coordinates)
    if(coordinates[2]>= self.canvas.winfo_width() or coordinates[0]<0):
      self.xVelocity = -self.xVelocity
    if(coordinates[3]>= self.canvas.winfo_height() or coordinates[1]<0):
      self.yVelocity = -self.yVelocity
    self.canvas.move(self.image, self.xVelocity,self.yVelocity)
window=Tk()
window.geometry('550x550')
canvas = Canvas(window,bg='aqua',height=HEIGHT, width=WIDTH)
canvas.pack()
volleyBall = Ball(canvas,0,0,100,1,1,'yellow')
tennisBall = Ball(canvas,0,0,5,4,3,'red')
footBall = Ball(canvas,0,0,100,2,1,'blue')
while True:
  volleyBall.move()
  tennisBall.move()
  footBall.move()
  time.sleep(0.01)  
  window.update()
window.mainloop()