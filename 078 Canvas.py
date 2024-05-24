from tkinter import *

window = Tk()
window.geometry('1000x1000')
canvas = Canvas(window,height=500,width=500,bg='aqua')
canvas.create_line(0,0,50,50, fill='blue',width=5)
canvas.create_line(0,500,250,250, fill='red',width=5)
canvas.create_rectangle(50,50,250,250, fill='purple')
points = (250,0,500,500,0,500)
canvas.create_polygon(points, fill='yellow', outline='black')
canvas.create_arc(0,0,500,500, fill='green')
canvas.create_arc(0,0,300,300, fill='purple',style=CHORD, start=270, extent = 180)
canvas.pack()

window.mainloop()