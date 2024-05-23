from tkinter import * 
from tkinter import messagebox    #messagebox is a submodule

def handleClick():
  messagebox.showinfo(title='Info', message='Showing info')
  messagebox.showwarning(title='Warning', message='Showing warning')
  messagebox.showerror(title='Error', message='Showing error')
  if messagebox.askokcancel(title= 'Ask ok/cancel', message ='Do you want to proceed?' ):
    print('You have proceeded')
  else:
    print('You have gone back')
  if messagebox.askretrycancel(title= 'Ask retry/cancel', message ='Do you want to retry?' ):
    print('You are retrying')
  else:
    print('You are not retrying')
  if messagebox.askyesno(title='Ask yes/no', message='Do you like the bike?'):
    print('You like the bike')
  else:
    print('You dont like the bike')
  if messagebox.askquestion(title='Ask question', message='Do you like the car?') == 'yes':
    print('You like the car')
  else:
    print('You dont like the car')
  print( messagebox.askyesnocancel(title='Ask yes/no/cancel', message='Do you like to code??', icon='warning'))

window = Tk()
button = Button(window,
                text='Click Me',
                command=handleClick)
button.pack()
window.mainloop()