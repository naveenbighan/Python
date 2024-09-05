import numpy as np

# a= np.array([1,2,3,4,5])
# print(a,type(a))

                 #mathematical operation

   #adding
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([5,10,15,20,25])
#    #+ operator
# # print(arr1+arr2)
#    # numpy method
# print(np.add(arr1,arr2))


    #subtracting
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([5,10,15,20,25])
#    #- operator
# # print(arr1-arr2)
#    # numpy method
# print(np.subtract(arr1,arr2))


  #multiplication
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([5,10,15,20,25])
#    #* operator
# print(arr1*arr2)
#    #numpy method
# print(np.multiply(arr1,arr2))   

  

  #division
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([5,10,15,20,25])
#  #  / operator
# print(arr2/arr1)

# print(np.divide(arr2,arr1))

  #power operator
# arr1=np.array([1,2,377,4,5])
# arr2=np.array([3])
#  # ** operator
# print(arr1**arr2)
#   # numpy method
# print(np.power(arr1,arr2))



# a=np.array([[1,2,3,4],[10,11,12,13],[14,15,16,17]],)
# print(a)
# print(np.insert(a,2,"2"))
# print(np.delete(a,2, axis=0))   

# #3d array
# a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a[1,1,2])




# arr=np.array([1,2,3,4,5,6])
# print(arr[::-1])

from numpy import random

x = random.choice([9, 5, 7, 3], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)


import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)


