def hello():
  print('Hello world')

# print(hello)    # prints mem address of funciton hello()
hi = hello
hi()
hello()
#print(hi)    # prints mem address of funciton hello()

say = print
say('This is working as if it were print')