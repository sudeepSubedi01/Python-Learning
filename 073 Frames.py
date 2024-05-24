from tkinter import *
window=Tk()
window.geometry('420x420')
frame = Frame(window, bg='pink', bd=5,relief= RAISED)
frame.place(x=100,y=100)
Button(frame, text='W', font=('Consolas',25), width=3).pack(side = 'top')
Button(frame, text='S', font=('Consolas',25), width=3).pack(side = 'left')
Button(frame, text='A', font=('Consolas',25), width=3).pack(side = 'left')
Button(frame, text='D', font=('Consolas',25), width=3).pack(side = 'left')

window.mainloop()