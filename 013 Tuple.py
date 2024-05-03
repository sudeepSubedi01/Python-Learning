student = ('victor',21,'male','victor')


print(student)
print(student.count('victor'))
print(student.index('male'))
print(student[2])

for i in student:
  print(i)

if 24 in student:
  print('the age is indeed 21')