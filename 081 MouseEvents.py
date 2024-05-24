from tkinter import *

def handleMouseEvent(event):
  # print('Clicked')
  print('(' + str(event.x) + ',' + str(event.y) + ')')

window=Tk()

# window.bind('<Button-1>',handleMouseEvent)
# window.bind('<ButtonRelease>',handleMouseEvent)
# window.bind('<Enter>',handleMouseEvent)
# window.bind('<Leave>',handleMouseEvent)
window.bind('<Motion>',handleMouseEvent)


window.mainloop()


#Button-1 : just click or right click
#Button-2 : scroll press
#Button-3 : right click