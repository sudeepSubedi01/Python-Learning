#--------------------------------------------------------
def new_game():
  guesses =[]
  correctGuesses = 0
  questionNum = 1

  for key in questions:
    print('------------------------------------')
    print(key)
    for i in options[questionNum - 1 ]:
      print(i)
    guess = input('Enter your choice: ').upper()
    guesses.append(guess)
    correctGuesses += check_answer(questions.get(key), guess)
    questionNum +=1  
  display_score(correctGuesses, guesses)
#--------------------------------------------------------
def check_answer(answer,guess):
  if (answer == guess):
    print("CORRECT!!")
    return 1
  else:
    print('INCORRECT')
    return 0
#--------------------------------------------------------
def display_score(correctGuesses, guesses):
  score = int((correctGuesses / len(questions)) *100 )
  print('------------------------------------')
  print('------------------------------------')
  print('RESULTS: ')
  print("Answers: ", end='')
  for value in questions.values():
    print(value, end=' ')
  print()
  print('Guesses: ', end='')
  for i in guesses:
    print(i, end=' ')
  print()
  print('Score: ' + str(score) + '%')
#--------------------------------------------------------
def play_again():
  playAgain = input("DO you wany to play again??(yes/no) ").upper()
  if (playAgain == 'YES'):
    return True
  else:
    return False
#--------------------------------------------------------
questions = {
    'Who created python?': 'A',
    'What year was Python created?': 'B',
    'Python is tributed to which comedy group?' :'C',
    'Is the Earth round?':'A'
  }

options=[
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "В. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
  ]
new_game()
while play_again():
  new_game()