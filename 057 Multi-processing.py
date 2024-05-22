from multiprocessing import Process, cpu_count
import time

def counter(num):
  count = 0
  while count< num:
    count +=1

#180000000
def main():
  print(cpu_count())    #return the number of cpu cores
  a = Process(target = counter, args = (45000000,))
  b = Process(target = counter, args = (45000000,))
  c = Process(target = counter, args = (45000000,))
  d = Process(target = counter, args = (45000000,))

  start_time = time.perf_counter()
  a.start()
  b.start()
  c.start()
  d.start()

  a.join()
  b.join()
  c.join()
  d.join()

  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  print('Finished in:', elapsed_time,' seconds')

if __name__ == '__main__':
  main()