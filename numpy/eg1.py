import numpy as np

# print(np.__version__) #check numpy version

# numpy is used to work with arrays. The array object in numpy is called ndarray
# we can create ndarray using array() function


# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# arr = np.array(42)
# arr = np.array([
#         [1, 2, 3], [4, 5, 6]
#     ])

# print(arr)
# print("type of array is: ", type(arr)) # check type of array
# print("number of dimension is: ", arr.ndim) # check number of dimension
# print("datatype is: ", arr.dtype) # check data types
x = [1,2,3,4]
y = [4,5,6,7]

z = np.add(x,y)
print(z)