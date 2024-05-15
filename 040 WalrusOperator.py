print(happy := True)

# foods = list()
# while True:
#   item = input('What food do you like?')
#   if (item == 'quit'):
#     break
#   foods.append(item)


foods = list()
while(( item := input('What food do you like? ')) != 'quit'):
  foods.append(item)
print(foods)