# var1 = orginalVariable[startIndex : stopIndex +1 : step]
#   startIndex is inclusive
#   stopIndex is exclusive
#   default startIndex is 0
#   step is optional
#   default step is 1
#   slice(startIndex, stopIndex)
name = "hari bahadur"

print(name[:3])   #all from start to index=2
print(name[4:])   #all from index=4 to end
print(name[0:4:1])  #starts from 0 upto 3 with step 1
print(name[5:12:1]) #starts from 5 upto 12 with step 1
print(name[::2])    #starts from 0 to end with step 2
print(name[::-1])   #starts from end to 0 with step 1

website1 = 'https://google.com'
website2 = 'https://facebook.com'
slice = slice(8,-4)

print(website1[slice])
print(website2[slice])

print(type(slice))