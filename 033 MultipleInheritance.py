class Prey:
  def flee(self):
    print('This animal flees')

class Predator:
  def hunt(self):
    print('This animal is hunting')

class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Prey, Predator):
  pass

r = Rabbit()
h = Hawk()
f = Fish()
r.flee()
h.hunt()
f.flee()
f.hunt()

