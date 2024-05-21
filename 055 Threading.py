import time
import threading

def eat_breakfast():
  time.sleep(3)
  print('You ate breakfast')
def drink_coffee():
  time.sleep(3)
  print('You drank coffee')
def study():
  time.sleep(2)
  print('You finished studying')

x = threading.Thread(target=eat_breakfast,args=())
x.start()
y = threading.Thread(target=drink_coffee,args=())
y.start()
z = threading.Thread(target=study,args=())
z.start()

x.join()
y.join()
z.join()
# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())   #returns the number of threads currently active
print(threading.enumerate)
print(time.perf_counter())