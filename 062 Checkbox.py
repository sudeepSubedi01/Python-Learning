from tkinter import *

def display():
  if(x.get() == 'YES'):
    print('You agreed!!')
  else:
    print('You dont agree!!!')

window = Tk()
photo = PhotoImage(file= 'python-logo.png')
# x = IntVar()
x= StringVar()
checkButton = Checkbutton(window,
                          text = 'I agree to the terms and conditions',
                          variable = x,
                          onvalue= 'YES',
                          offvalue= 'NO',
                          command=display,
                          font=('Arial',20),
                          fg='#00FF00',
                          bg='black',
                          activebackground='black',
                          activeforeground='green',
                          padx=25,
                          pady=10,
                          image = photo,
                          compound='top'
                          )
checkButton.pack()
window.mainloop()