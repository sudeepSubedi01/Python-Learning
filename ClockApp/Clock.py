from tkinter import *
import time

def updateTime():
  timeString = time.strftime('%I:%M:%S %p')
  timeLabel.config(text= timeString)
  dayString = time.strftime('%A')
  dayLabel.config(text= dayString)
  timeLabel.after(1000,updateTime)
window = Tk()
timeLabel = Label(window, font=('Arial',50),fg='#00FF00', bg='black')
timeLabel.pack()
dayLabel = Label(window, font=('Ink Free',50))
dayLabel.pack()
updateTime()
window.mainloop()