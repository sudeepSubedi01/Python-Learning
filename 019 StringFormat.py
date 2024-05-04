#-----------directly formatting and displaying-------------
animal = 'cow'
item = 'moon'
print('The ' + animal + ' jumped over the ' + item)
print('The {} jumped over the {}'.format(animal, item))   #positional argument
print('The {1} jumped over the {0}'.format(animal, item)) #positional argument
print('The {animal1} jumped over the {item1}'.format(animal1='buffalo', item1 = 'sun')) #keyword argument

#-----------string in a variable and formatting-------------
text = 'The {} flew over the {}'  #index or key can be given inside braces
print(text.format('bird', 'bus'))

text1 = 'The {1} flew over the {2}'
print(text1.format('hen', 'eagle', 'house'))

text2 = 'The {animal2} flew over the {item2}'
print(text2.format(animal2='dragon', item2='jungle'))

#-------------padding to the text-------------------
name = 'Biden'
print('Hello, this is {}. Nice to meet you!!'.format(name))
print('Hello, this is {name3:10}. Nice to meet you!!'.format(name3 = 'Trump'))  #leaves padding to the right
print('Hello, this is {:<10}. Nice to meet you!!'.format(name))   #left alignment
print('Hello, this is {:>10}. Nice to meet you!!'.format(name))   #right alignment
print('Hello, this is {:^10}. Nice to meet you!!'.format(name))   #center alignment


#----------------number formatting--------------------
number1 = 3.149343
print('The number is {:.2f}'.format(number1))

number2 = 10000
print('The number is {:,}'.format(number2))

number3 = 15
print('The number is {:b}'.format(number3))
print('The number is {:o}'.format(number3))
print('The number is {:X}'.format(number3))
print('The number is {:elll}'.format(number3))
