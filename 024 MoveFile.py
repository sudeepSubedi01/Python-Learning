import os
source = 'sample-copy.txt'
destination = 'D:\\Python\\TestFolder\\newSample-copy.txt'

try:
  if(os.path.exists(destination)):
    print('A file with same name exists already')
  else:
    os.replace(source, destination)
    print('file moved')
    
except FileNotFoundError as e:
  print(e)
  print('File not opened properly')
