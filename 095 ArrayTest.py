# The following doesnt work:
arr1 = [1,2,3,4,5]
arr2 = []
# for i in range(len(arr1)):
#   arr2[i] = arr1[i]
# Reason: Lists in Python do not automatically expand to accommodate new indices when you assign values to them directly.
# The solution: 
arr2 = arr1.copy()
print(arr2)

#------------------------------------------------------------------------------
arr3 = [10,11,12,13,14,15]
# arr3[6]= 16 #this doesnt work
arr3.append(56)
print(arr3)
