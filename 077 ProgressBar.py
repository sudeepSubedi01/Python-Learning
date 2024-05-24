from tkinter import *
from tkinter.ttk import *
import time

def handleDownload():
  totalSize = 100
  downloaded = 0
  speed=2
  while(downloaded<totalSize):
    time.sleep(0.5)
    bar['value'] += (speed/totalSize)*100
    downloaded +=speed
    percentage.set(str(int(downloaded/totalSize *100)) + ' %')
    text.set(str(downloaded) + ' out of ' + str(totalSize) + ' completed')
    window.update_idletasks()
window = Tk()
percentage = StringVar()
text = StringVar()
window.geometry('420x420')
textLabel = Label(window,textvariable=text).pack()
bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)
percentLabel = Label(window,textvariable=percentage).pack()
button=Button(window, text='Download', command=handleDownload).pack()
window.mainloop()