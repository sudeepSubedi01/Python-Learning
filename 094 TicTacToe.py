from tkinter import *
import random

def nextTurn(row,column):
  global player
  if((buttons[row][column]['text'] == '') and checkWinner() is False):
    if player == players[0]:
      buttons[row][column]['text'] = player
      if checkWinner() is False:
        player = players[1]
        label.config(text= players[1]+ ' turn')
      elif checkWinner() is True:
        label.config(text= players[0]+ ' wins')
      elif checkWinner() == 'Tie':
        label.config(text = 'Tie!!!')
    else:
      if player == players[0]:
        buttons[row][column]['text'] = player
      if checkWinner() is False:
        player = players[0]
        label.config(text= players[0]+ ' turn')
      elif checkWinner() is True:
        label.config(text= players[1]+ ' wins')
      elif checkWinner() == 'Tie':
        label.config(text = 'Tie!!!')
    
def checkWinner():
  for row in range(3):
    if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != ' ':
      return True

  for column in range(3):
    if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != ' ':
      return True 
  
  if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' ':
    return True
  elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != ' ':
    return True
  elif emptySpace() is False:
    return 'Tie'
  else:
    return False
  
def emptySpace():
  pass

def newGame():
  pass

window = Tk()
window.geometry('500x700')
window.title('Tic Tac Toe Game')
players = ['x','o']
player = random.choice(players)
# print (player)
buttons = [[0,0,0],[0,0,0],[0,0,0]]
label = Label(window,text = player+' Turn', font=('Consolas',40))
label.pack(side='top')
resetButton = Button(window,text='Restart game', font=('Consolas',20),command=newGame)
resetButton.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
  for column in range(3):
    buttons[row][column] = Button(frame,text ='', font=('Consolas',40), width=5,height=2, command=lambda row=row,column=column:nextTurn(row,column))
    buttons[row][column].grid(row=row,column=column)
window.mainloop()