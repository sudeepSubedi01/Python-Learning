names = [ 'hello', 'world', 'nepal', 'india']
print( names)
print(names[3])

#changing content of list
names[3] = 'usa'
print(names[3])


names.append('bhutan') #adds to last
names.remove('nepal')
names.insert(2,'america')
names.sort()
#displaying whole list
for i in names:
  print(i)

print("Last element is: " + names.pop())

print(type(names)) #list