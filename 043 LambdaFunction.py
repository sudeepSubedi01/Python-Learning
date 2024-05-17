def double(x):
  return x*2
print(double(5))

double = lambda x:x*2
print(double(7))

multiply = lambda x,y : x*y
print(multiply(1,6))

add = lambda a,b,c : a+b+c
result = add(1,5,8)
print(result)

fullName = lambda firstName, lastName : firstName+ ' ' +lastName
print(fullName('hello', 'world'))

ageCheck = lambda age : 'Eligible to vote' if age>= 18 else 'Not eligible to vote'
print(ageCheck(15))
print(ageCheck(55))