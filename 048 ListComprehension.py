squares = []
for i in range (1,11):
  squares.append(i*i)
print(squares)

#-----------------------------------------------------------
#using list comprehension
squareNums = [i*i for i in range (3,11)]
print(squareNums)

#-----------------------------------------------------------
#mimicing certain lambda functions
marks = [100,90,80,70,60,50,40,30,0]
passed = list(filter(lambda x: x>=60 , marks))
print(passed)

#-----------------------------------------------------------
marks1 = [100,90,80,70,60,50,40,30,0]
passed1 = [i for i in marks1 if i>=60]
print(passed1)

#-----------------------------------------------------------
marks2 = [100,90,80,70,60,50,40,30,0]
passed2 = [i if i>=60 else 'FAILED' for i in marks2]
print(passed2)