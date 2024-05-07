import random

moves = ['rock','paper', 'scissors']
computerMove = random.choice(moves)

while True:
  playerMove = ''
  while playerMove not in  moves:
    playerMove = input('Enter your move: ').lower()

  if(computerMove == playerMove ):
    print('Computer: ' + computerMove)
    print('Player: '+ playerMove)
    print('Game Tie!!!!')
  elif(playerMove == 'rock'):
    if(computerMove == 'scissors'):
      print('Computer: ' + computerMove)
      print('Player: '+ playerMove)
      print('You win!!!!')
    if(computerMove == 'paper'):
      print('Computer: ' + computerMove)
      print('Player: '+ playerMove)
      print('You lose!!!!')
  elif(playerMove == 'paper'):
    if(computerMove == 'scissors'):
      print('Computer: ' + computerMove)
      print('Player: '+ playerMove)
      print('You lose!!!!')
    if(computerMove == 'rock'):
      print('Computer: ' + computerMove)
      print('Player: '+ playerMove)
      print('You win!!!!')
  elif(playerMove == 'scissors'):
    if(computerMove == 'paper'):
      print('Computer: ' + computerMove)
      print('Player: '+ playerMove)
      print('You win!!!!')
    if(computerMove == 'rock'):
      print('Computer: ' + computerMove)
      print('Player: '+ playerMove)
      print('You lose!!!!')
  
  playAgain = input('Want to play again?? (yes/no)').lower()
  if (playAgain == 'no' ):
    break

print('End of game')

