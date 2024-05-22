import threading
import time

def timer():
  print()
  count = 0
  while True:
    time.sleep(1)
    count+=1
    print('Logged in for: '+ str(count) + ' seconds')

x = threading.Thread(target= timer )
# x.setDaemon(True)   #deprecated
x.daemon = True
x.start()
# print(x.isDaemon())   #deprecated
print(x.daemon)

answer = input("Input sth to exit this background task:")