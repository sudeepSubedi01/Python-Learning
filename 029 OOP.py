class Car:
  def drive(self):
    print('The car ' + self.name + ' is driving')

  def stop(self):
    print("The car has stopped")

  def __init__(self,name, model,year, color):
    self.name = name
    self.model = model
    self.year = year
    self.color = color

car_1 = Car('Chevy','Corvette',2021, 'blue')
car_2 =  Car('Ford', 'Mustang', 2022,'Red')

print(car_1.name)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

print(car_2.name)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()