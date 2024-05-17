students = ['hello3', 'hello5', 'hello1', 'hello4', 'hello2', 'hello6']
students.sort(reverse=True)
for i in students:
  print(i)

#----------------------------------------------------------------------------------
print()
print()
print()
people = ['hello3', 'hello5', 'hello1', 'hello4', 'hello2', 'hello6']
sortedPeople = sorted(people, reverse=False)
for i in sortedPeople:
  print(i)

#----------------------------------------------------------------------------------
print()
print()
print()
student = [
  ('hello5', 'F', 69),
  ('hello1', 'A', 66),
  ('hello2', 'C', 42),
  ('hello4', 'E', 1),
  ('hello6', 'B', 100),
  ('hello3', 'D', 55)
  ]
value = lambda col: col[1]
student.sort(key = value)
for i in student:
  print(i)

#a single tuple is passed as an argument to col
#value function returns column 2 data to the value function
#these column 2 data are then passed to sort method and sorting is done based on this

#----------------------------------------------------------------------------------
print()
print()
print()
student1 = [
  ('hello5', 'F', 69),
  ('hello1', 'A', 66),
  ('hello2', 'C', 42),
  ('hello4', 'E', 1),
  ('hello6', 'B', 100),
  ('hello3', 'D', 55)
  ]
value = lambda col: col[2]
student1.sort(key = value)
for i in student1:
  print(i)