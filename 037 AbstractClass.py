from abc import ABC, abstractmethod

class vehicle(ABC):
  @abstractmethod
  def go(self):
    pass

  @abstractmethod
  def stop(self):
    pass

class car(vehicle):
  def go(self):
    print('You drive the car')
  def stop(self):
    print('This car has stopped')

class motorcycle(vehicle):
  def go(self):
    print('You ride motorcycle')
  def stop(self):
    print('This motorcycle has stopped')

# v = vehicle()
c = car()
m = motorcycle()

# v.go()
c.go()
m.go()
c.stop()
m.stop()