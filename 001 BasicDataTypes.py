print("hello world")
print(25 + 23)
print(256.32456)
print(False + True)
print(False * True)
print(4+3j)

fname = "Hari"
mname = "Bahadur"
lname = "Khadka"
name = fname +' ' + mname + ' '+ lname
age = 25 * 3
salary = 5012.236
val = False * True
cmplx = 5+696j - 2 + 1j

print("The name is : " + fname + mname + lname +' ' + str(age) +' ' + str(salary) )
print(val)
print("The boolean value is: " + str(val))
print("Full name is: "+ name)
print('The complex number is: '+ str(cmplx))

print(type(name)) 	  #str
print(type(age))
print(type(salary))
print(type(val))      #bool
print(type(cmplx))    #complex