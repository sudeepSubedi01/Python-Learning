from tkinter import *

def handleDrag(event):
  widget = event.widget
  widget.startX = event.x    #custom attribute added to the label widget
  widget.startY = event.y
  print(str(event.x) + str(event.y))
def handleMotion(event):
  widget = event.widget
  x = widget.winfo_x() - widget.startX + event.x    #parent element is window
  y = widget.winfo_y() - widget.startY + event.y
  widget.place(x=x,y=y)

window = Tk()
window.geometry('420x420')
label1 = Label(window,bg='red',width=10,height=5)
label1.place(x=0,y=0)
label2 = Label(window,bg='blue',width=10,height=5)
label2.place(x=200,y=200)
label1.bind('<Button-1>',handleDrag)
label1.bind('<B1-Motion>',handleMotion)
label2.bind('<Button-1>',handleDrag)
label2.bind('<B1-Motion>',handleMotion)
window.mainloop()