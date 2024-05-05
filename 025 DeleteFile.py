import os
filePath = 'D:\\Python\\TestFolder\\newSample-copy.txt'
try:
    os.remove(filePath)
    print('file deleted')

except Exception as e:
  print(e)