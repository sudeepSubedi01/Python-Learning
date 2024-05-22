from tkinter import *

window = Tk()
window.geometry('900x420')
photo = PhotoImage(file = 'python-logo.png')

label = Label(window,
              text = 'hello world, this is my new home from now on',
              font=('Arial',40,'bold'), 
              fg = '#00FF00', 
              # bg='black',
              relief =RAISED,
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound = 'bottom')
label.pack()    #places label at the center of the window
# label.place(x=100,y=100)
window.mainloop()
print(type(window))     #type of window is tkinter.Tk
print(type(label))     #type of window is tkinter.Label