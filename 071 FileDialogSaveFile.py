from tkinter import *
from tkinter import filedialog

def handleSave():
  txtInput = textArea.get(1.0, END)
  print(txtInput)
  file = filedialog.asksaveasfile(initialdir='D:\\Python',
                                  defaultextension='.txt',
                                  filetypes=[
                                    ('Text File', '.txt'),
                                    ('HTML file', '.html'),
                                    ('All files', '.*')
                                  ])
  if file is None:
    return
  #txtInput = input('Enter some text to write to a file:')
  file.write(txtInput)
  file.close()
window = Tk()
window.geometry('420x420')
textArea = Text(window,
                font=('Ink Free',15),
                height = 10,
                width = 20,
                bg='aqua',
                fg='blue')
textArea.pack()
button = Button(window,
                text = 'Save',
                command= handleSave)
button.pack()
window.mainloop()