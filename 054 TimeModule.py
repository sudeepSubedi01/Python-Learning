import time

print(time.time())
print(time.ctime(100000000))
print(time.ctime(time.time()))

print(time.strftime('%B %d %Y %H:%M:%S', time.localtime()))

time_string = '20 April 2020'
time_object = time.strptime(time_string, '%d %B %Y')
print(time_object)
