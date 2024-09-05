import numpy as np 

# train_set=np.array([1, 2, 3])
# test_set=np.array([[0, 1, 2], [1, 2, 3]])

# resulting_set = np.vstack([train_set, test_set])
# print(resulting_set)


# arr=np.array([4, 3, 2, 4, 5,8,1])
# N= 3
# print(arr.argsort( ) [ -N: ][: : -1])


train_set = np.array([1, 2, 3])
test_set = np.array([[0, 1, 2], [1, 2, 3]])
res_set= np.vstack([train_set,test_set])
print(res_set)