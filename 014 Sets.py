#set 1
foods = {'burger', 'rice', 'roti', 'beer','water','beer'}
print (foods)

foods.add('milk')
foods.remove('roti')
print(foods.pop())
print(len(foods))
# foods.clear()
print('using loop:')
for i in foods:
  print(i)

#set 2
dishes = {'cup','bottle','plate', 'beer'}
foods.update(dishes)
dishes.update(foods)

print(foods)
print(dishes)


#set 3
foods1 = {'dal', 'pizza', 'chocolate', 'samosa','vodka','vodka'}
dishes1 = {'cooker','thermos','jug', 'bucket','vodka'}

union = foods1.union(dishes1)
# sum = dishes.union(foods)
print(union)

#set 4
intersection = foods1.intersection(dishes1)
print(intersection)

#set 5
difference = foods1.difference(dishes1)
print(difference)

