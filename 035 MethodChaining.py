class car:
  def turnOn(self):
    print("You start the engine")
    return self
  def drive(self):
    print("You drive the car")
    return self
  def brake(self):
    print('You step on the brakes')
    return self
  def turnOff(self):
    print('You turn off the engine')
    return self

c = car()
c.turnOn()
c.drive()
print()
c.turnOn().drive()
print()
c.brake().turnOff()
print()
c.turnOn().drive().brake().turnOff()