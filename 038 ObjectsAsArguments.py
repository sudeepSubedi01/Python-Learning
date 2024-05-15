class Car:
  color = None

class Motorcycle:
  color = None

def changeColor(vehicleObj,color):
  vehicleObj.color = color

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()

changeColor(car1, 'red')
changeColor(car2, 'blue')
changeColor(car3, 'black')
changeColor(bike1, 'green')

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)