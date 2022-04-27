# import array 
 
# # creating an array with integer type
# arr = array.array('i', [1, 2, 3, 1, 5])
 
# # printing original array
# print ("The new created array is : ", end =" ")
# for i in range (0, 3):
#     print (arr[i], end =" ")
# print()

# print ("Array before insertion : ", end =" ")
# for i in range (0, 3):
#     print (arr[i], end =" ")
# print()
 
# # inserting array using
# # insert() function
# arr.insert(1, 4)
 
# print ("Array after insertion : ", end =" ")
# for i in (arr):
#     print (i, end =" ")
# print()

# # using pop() to remove element at 2nd position
# print ("The popped element is : ", end ="")
# print (arr.pop(2))
 
# # printing array after popping
# print ("The array after popping is : ", end ="")
# for i in range (0, 4):
#     print (arr[i], end =" ")
# print("\r")

# # using remove() to remove 1st occurrence of 1
# arr.remove(1)
 
# # printing array after removing
# print ("The array after removing is : ", end ="")
# for i in range (0, 3):
#     print (arr[i], end =" ")
# print()

# # updating a element in a array
# arr[2] = 60
# print("Array after updation : ", end ="")
# for i in range (0, 4):
#     print (arr[i], end =" ")
# print()


#NUMPY
# import numpy as np
#NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python. It contains various features

# arr = np.array( [[ 1, 2, 3],
                #  [ 4, 2, 5]] )
 
# Printing type of arr object
# print("Array is of type: ", type(arr))
 
# Printing array dimensions (axes)
# print("No. of dimensions: ", arr.ndim)
 
# Printing shape of array
# print("Shape of array: ", arr.shape)
 
# Printing size (total number of elements) of array
# print("Size of array: ", arr.size)
 
# Printing type of elements in array
# print("Array stores elements of type: ", arr.dtype)

# Creating array from list with type float
# a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
# print ("Array created using passed list:\n", a)
 
# Creating array from tuple
# b = np.array((1 , 3, 2))
# print ("\nArray created using passed tuple:\n", b)
 
# Creating a 3X4 array with all zeros
# c = np.zeros((3, 4))
# print ("\nAn array initialized with all zeros:\n", c)
 
# Create a constant value array of complex type
# d = np.full((3, 3), 6, dtype = 'complex')
# print ("\nAn array initialized with all 6s."
#             "Array type is complex:\n", d)
 
# Create an array with random values
# e = np.random.random((2, 2))
# print ("\nA random array:\n", e)

# Creating array from list with type float
# a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
# print ("Array created using passed list:\n", a)
 
# Creating array from tuple
# b = np.array((1 , 3, 2))
# print ("\nArray created using passed tuple:\n", b)
 
# Creating a 3X4 array with all zeros
# c = np.zeros((3, 4))
# print ("\nAn array initialized with all zeros:\n", c)
 
# Create a constant value array of complex type
# d = np.full((3, 3), 6, dtype = 'complex')
# print ("\nAn array initialized with all 6s."
#             "Array type is complex:\n", d)
 
# Create an array with random values
# e = np.random.random((2, 2))
# print ("\nA random array:\n", e)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# flarr = arr.flatten()
 
# print ("\nOriginal array:\n", arr)
# print ("Fattened array:\n", flarr)