def hello(name):
  print('hello ' + name)
  print('have a nice day')

print('calling the function')
hello("victor")
name1 = 'paudel'
hello(name1)

#--------return statement---------
def addition(a,b):
  return a+b
result = addition(5,6)
print(result)

#--------arguments---------
def hello1(first, middle, last):
  print('Hello ' + first+ " " + middle + " " + last)

hello1('Victor','Joe','Biden')                            #positional argument
hello1(last = 'Victor', first = 'Joe',middle = 'Biden')   #keyword argument

#--------nested function calls---------
# num = input('Enter a whole positive number: ')
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
print(round(abs(float(input('Enter a whole number: ')))))
