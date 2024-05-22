from tkinter import *


window = Tk()   #instantiate and instance of a window
window.geometry("420x420")
window.title('058 GUI-Windows')
icon = PhotoImage(file = 'python-logo.png')
window.iconphoto(True, icon)
window.config(background='aqua')

window.mainloop()   #places window on computer screen, listens for events