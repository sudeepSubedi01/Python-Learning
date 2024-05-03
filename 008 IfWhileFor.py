import time

age = int(input('Enter your age: '))
if(age<=10):
  print('You are a child')
elif(age == 100):
  print("You have reached century")
elif (age>10):
  print('You are adolescent')
else:
  print('You are adult')

name=''
while(len(name) == 0 ):
  name=input('Enter your name: ')

for i in range (10):
  print(i)

for i in range(50,60+1,2):
  print(i)

for i in 'Hello World':
  print(i)

for num in range(10,0,-1):
  print (num)
  time.sleep(2)
print('happy birthday')