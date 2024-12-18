from tkinter import * 
from tkinter import colorchooser
from tkinter import filedialog
import pyautogui as pg
from tkinter import messagebox
import pyperclip
from tkinter import font

def handleColorChange():
  color = colorchooser.askcolor()
  print(color[1])
  textField.config(fg=color[1])

def handleFontChange(*args):
  textField.config(font=(fontName.get(),fontSpinBox.get()))

def handleSave():
  inputText = textField.get('1.0', END)
  print(inputText)
  file = filedialog.asksaveasfile(initialdir='D:\\Python',
                                  defaultextension='.txt',
                                  filetypes=[
                                    ('Text files','.txt'),
                                    ('HTML file','.html')
                                  ])
  file.write(inputText)
  file.close()

def handleOpen():
  file = filedialog.askopenfile(initialdir='D:\\Python',
                                defaultextension='.txt',
                                filetypes=[
                                  ('Text files','.txt'),
                                  ('HTML file','.html')
                                ])
  readTxt = file.read()
  textField.delete(1.0, END)
  textField.insert(1.0,readTxt)
  file.close()
                                
def handleClear():
  textField.delete(1.0,END)

def handleQuit():
  window.destroy()

def handleCopy():
  inputTxt = textField.get(1.0,END)
  window.clipboard_clear()
  window.clipboard_append(inputTxt)
  print(messagebox.showinfo(title = 'Copy',message= 'Copied to clipboard'))

def handleCut():
  inputTxt = textField.get(1.0,END)
  window.clipboard_clear()
  window.clipboard_append(inputTxt)
  print(messagebox.showinfo(title = 'Copy',message= 'Copied to clipboard'))
  textField.delete(1.0, END)

def handlePaste():
  clipboardText = pyperclip.paste()
  textField.insert(END,clipboardText)


window = Tk()
fontSize = StringVar(window)
fontSize.set('25')
fontName = StringVar(window)
fontName.set('Arial')
window.geometry('500x500')
window.minsize(500,500)
menubar = Menu(window)
window.config(menu = menubar)
fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Save',command=handleSave)
fileMenu.add_command(label='Open', command=handleOpen)
fileMenu.add_command(label='Quit',command=handleQuit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Copy',command=handleCopy)
editMenu.add_command(label='Paste',command=handlePaste)
editMenu.add_command(label='Cut',command = handleCut)

textField = Text(window,
                 bg='light yellow',
                 font=('Consolas',25),
                 height = 7,
                 width=20,
                 pady=5)
textField.pack(expand=True,fill=BOTH)

frame = Frame(window)
frame.pack()
colorBtn = Button(frame,text='Color',command=handleColorChange)
colorBtn.pack(side=LEFT)
fontSpinBox = Spinbox(frame,from_=10, to=30, textvariable=fontSize,command=handleFontChange)
fontSpinBox.pack(side=LEFT)
fontOption = OptionMenu(frame,fontName,*font.families(),command=handleFontChange)
fontOption.pack(side=LEFT)
clearBtn = Button(frame,text='Clear',command=handleClear)
clearBtn.pack(side=LEFT)

window.mainloop()