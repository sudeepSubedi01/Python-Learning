import os

filePath =  'D:\\Python\\sample.txt'
dir = 'D:\\Python'
if (os.path.exists(filePath)):
  print('The location exists')
else:
  print('The location does not exist')

print(os.path.isfile(filePath))
print(os.path.isdir(dir))
print(os.getcwd())
print(os.listdir(path='.'))

with open (filePath) as f:
  print()
  print(f.read())