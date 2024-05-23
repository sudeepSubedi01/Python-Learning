from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']

def handleSelect():
  if (x.get() == 0):
    print('You ordered pizza')
  elif(x.get() == 1):
    print('You ordered hamburger')
  else:
    print('You ordered hotdog')
window =Tk()
photo = PhotoImage(file='python-logo.png')
x = IntVar()
window.geometry('420x420')
for index in range(len(food)):
  radioBtn = Radiobutton(window,
                         text=food[index],    #adds text to radio buttons
                         variable= x,         #groups radio buttons together if thery share same variable
                         value = index,       #assigns each radio button a different value 
                         padx=25,
                         font = ('Impact',25),
                         image= photo,
                         compound='bottom',
                         command=handleSelect        
                         )
  radioBtn.pack(anchor=W)
window.mainloop()