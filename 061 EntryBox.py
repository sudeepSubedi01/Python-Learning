from tkinter import *

def handleSubmit():
  username = entry.get()
  print(username)
  entry.config(state = DISABLED)
def handleDelete():
  entry.delete(0,END)
def handleBackspace():
  entry.delete(len(entry.get())-1,END)

window = Tk()
entry = Entry(window,
              font = ('Arial', 30),
              bd=4,
              fg='#00FF00',
              bg='black',
              show='*')
entry.insert(0,'TYPE HERE')
entry.pack(side=LEFT)

submit_button = Button(window,
                       text = 'Submit',
                       font = 'Arial',
                       bd = 2,
                       command = handleSubmit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text = 'Delete',
                       font = 'Arial',
                       bd = 2,
                       command = handleDelete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                          text = 'Backspace',
                          font = 'Arial',
                          bd = 2,
                          command = handleBackspace)
backspace_button.pack(side = RIGHT)
window.mainloop()