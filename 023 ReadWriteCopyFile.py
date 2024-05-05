import shutil
try:
  with open('sample.txt') as file:
      print("First line:")
      print(file.readline())  # reads first line and print it
      print()

      print("Remaining lines:")
      print(file.readlines())  # Reads all remaining lines and print them as a list
      print()

      print("Entire file content:")
      print(file.read())  # Reads entire file and print its contents
  
  with open('sample.txt', 'w') as f:
     f.write('this is my file \n This file is very good file \n how much good is this file')

  with open('sample1.txt', 'a') as ff:
     ff.writelines(['hello world1', 'hello world2', 'hello world3'])
  
except Exception as e:
   print(e)
   print('Sth went wrong')

shutil.copy('D:\\Python\\sample.txt','D:\\Python\\sample-copy.txt' )