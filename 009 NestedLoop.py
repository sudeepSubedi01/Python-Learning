rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of columns: '))
symbol = input("Enter the symbol you want to display: ")

for i in range (rows):
  for j in range(cols):
    print(symbol, end = '')
  print()