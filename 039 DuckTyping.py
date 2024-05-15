class Duck:
  def walk(self):
    print('This duck is walking')
  def talk(self):
    print('This duck is quacking')

class Chicken:
  def walk(self):
    print('This chickn is walking')
  def talk(self):
    print('This chicken is clucking')

class Person:
  def catch(self, duckObj):
    duckObj.walk()
    duckObj.talk()
    print("You caught it")

d = Duck()
c = Chicken()
p = Person()

p.catch(c)