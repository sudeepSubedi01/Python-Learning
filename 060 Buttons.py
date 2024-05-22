from tkinter import *

count= 0
def handleClick():
    global count
    count = count +1
    print(f'Count: {count}')

window = Tk()
window.geometry('420x420')

photo = PhotoImage(file='python-logo.png')
button = Button(window, 
                text='Click this button',
                command=handleClick,
                font=('Comic Sans', 30),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound = 'bottom')
button.pack()

window.mainloop()
