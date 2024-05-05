import random

print(random.randint(1,5))  #returns a random integer number
print(random.random())      #returns a random number between 0 and 1
# print(random.randrange(1,15,2))


myList = ['rock', 'paper','scissors']
print(random.choice(myList))

cards = [1,2,3,4,5,6,7,8,9,'J','K','Q','A']
random.shuffle(cards)
print(cards)