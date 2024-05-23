from tkinter import *

def handleSubmit():
  txtInput = txtArea.get('1.0', END)
  print(txtInput)
window = Tk()
txtArea = Text(window,
               bg='light yellow',
               fg='purple',
               font=('Ink Free',25),
               height=8,
               width=20,
               padx=20,
               pady=20
               )
txtArea.pack()
button = Button(window,
                text='Submit',
                command=handleSubmit)
button.pack()
window.mainloop()