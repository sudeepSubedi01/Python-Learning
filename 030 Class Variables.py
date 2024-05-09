class Car:
  wheels = 4 #class variables

  def drive():
    print('The car is driving')
  def stop():
    print('The car has stopped')
  def __init__(self, name, model,year, color):
    self.name = name      #instance variables
    self.model = model
    self.year = year
    self.color = color
    # self.wheels = 5

car1 = Car('Chevy','Corvette',2021, 'blue')
car2 = Car('Ford', 'Mustang', 2022,'Red')
print(car1.wheels)
print(car2.wheels)