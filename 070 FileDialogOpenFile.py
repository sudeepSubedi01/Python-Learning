from tkinter import *
from tkinter import filedialog

def handleOpen():
  filepath = filedialog.askopenfilename(initialdir='D:\\Python', 
                                        title='OPEN A FILE ASAP!!!',
                                        filetype=(('text files', '*.txt'),('all files','*.*')))
  # print(filepath)
  file = open(filepath,'r')
  print(file.read())
  file.close()
window = Tk()
button = Button(window,
                text='Open file',
                command=handleOpen)
button.pack()
window.mainloop()