student = ('victor',21,'male','victor')


print(student)
print(student.count('victor'))
print(student.index('male'))

for i in student:
  print(i)

if 24 in student:
  print('the age is indeed 21')