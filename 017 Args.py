#---------args in python-----------
def sum(*args):
  print(args)
  sum = 0
  for i in args:
    sum = sum + 1
    return sum
  
print(sum(3,5,5,8,7,1))