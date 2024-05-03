#use of break
while True:
  name = input("Enter your name: ")
  if name!='':
    break


#use of continue
phone = '123-456-789'
for i in phone:
  if i == '-':
    continue
  else:
    print(i , end='')
print()
#use of pass
for i in range(4,25):
  if i==13:
    continue
  else:
    print(str(i) + ' ' , end='')