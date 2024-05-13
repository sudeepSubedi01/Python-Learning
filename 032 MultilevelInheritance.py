class organism:
  alive = True

class animal(organism):
  def eat(self):
    print('This animal is sleeping')

class dog(animal):
  def bark(self):
    print('This dog is barking')

d = dog()
print(d.alive)
d.eat()
d.bark()
