def hello (**kwargs):
  kwargs.update({'title' : 'Mr. Prime Minister'})
  print(kwargs)
  print("Hello ",end = '' )
  for key,value in kwargs.items():
    print(value, end = ' ')

hello(title='Mr. President',first = 'Victor', middle='John', last= 'Biden')