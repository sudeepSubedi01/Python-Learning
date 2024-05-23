import tkinter

def handleSubmit():
  # print(type(scale.get()))
    print('The temperature is: ' + str(scale.get()) + ' degrees C')

window = tkinter.Tk()
hotlabel = tkinter.Label(window,
                         text='HOT',
                         font = ('Impact',25))
hotlabel.pack()
scale = tkinter.Scale(window, 
                      from_=100, 
                      to=0,
                      length = 600,
                      orient= 'vertical',
                      font = ('Consolas',20),
                      tickinterval_ = 10,    #adds numeric indicators for value
                      showvalue=1,           #show/hide current value
                      resolution=5,          #increment of slider
                      troughcolor = '#69EAFF',
                      fg='#FF1C00'
                      )
scale.pack()
coldlabel = tkinter.Label(window,
                         text='COLD',
                         font = ('Impact',25))
coldlabel.pack()
button = tkinter.Button(window,
                        text='Print Temperature',
                        command= handleSubmit)
button.pack()
window.mainloop()