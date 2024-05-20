import functools
#from functools import reduce
letters = ['H','E','L','L','O']
word = functools.reduce(lambda x,y : x+y, letters)
print(word)

# H + E = HE
# HE + L = HEL
# HEL + L = HELL
# HELL + O = HELLO
# word = HELLO

#---------------------------------------------------------------
num = [5,4,3,2,1]
factorial = functools.reduce(lambda x,y : x * y , num)
print(factorial) 