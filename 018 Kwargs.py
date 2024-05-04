def hello (**kwargs):
  print(kwargs)
  print("Hello ",end = '' )
  for key,value in kwargs.items():
    print(value, end = ' ')

hello(title='Mr. President',first = 'Victor', middle='John', last= 'Biden')