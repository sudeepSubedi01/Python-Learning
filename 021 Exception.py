try:
  numerator = int(input('Enter numerator: '))
  denominator = int(input('Enter denominator: '))
  result = numerator / denominator

except ZeroDivisionError as e:         #catches all exception
  print(e)
  print('Division cant be done by zero')

except ValueError as e:   
  print(e)
  print('Numbers only allowed')

except Exception as e:         #catches all exception
  print(e)
  print('Something went wrong')
else:
  print (result)
finally:
  print('This finally block will always execute')