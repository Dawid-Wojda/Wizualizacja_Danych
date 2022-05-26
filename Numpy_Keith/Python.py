import numpy as np
# a = np.array([1, 2, 3], dtype='int16')
# print(a)
# b = np.array([[9.0, 8.0, 7.0,], [6.0, 5.0, 4.0]])
# print(b)
#
# print("\n")
# print(b.ndim)
# print(a.ndim)
#
# print("\n")
# print(a.shape)
# print(b.shape)
#
# print("\n")
# print(a.size)
# print(b.size)

# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a)
# print("\n")
#
# #Get a specific element
# print(a[1, 3])
#
# #Get a specfic row
# print(a[0, :])
#
# #Get a specific column
# print(a[:,4])
#
# print("\n")
# print(a[0, 0:5:2])
#
# a[0,0] = 25
# print(a)
# print("\n")
#
# a[1,:] = 8
# print(a)

# a = np.zeros((4,5))
# print(a)
# b = np.ones((4,5))
# print("\n")
# print(b)
# print("\n")
# c = np.full((4, 5), (50))
# print(c)
# print("\n")
# d = np.random.rand(2,3)
# print(d)
# print("\n")
# print(np.random.randint(2, 10, size = (4,4)))
# print(np.identity(8))
# print("\n")
#
# c = np.array([[1, 2, 3]])
# c1 = np.repeat(c,3, axis=0)
# print(c1)

# a = np.ones((5,5))
# b = np.zeros((3,3))
# # print(a)
# # print(b)
# b[1,1] = 9
# a[1:4, 1:4] = b
# print(a)

# a = np.array([1, 2, 3])
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)

# MATH
# a = np.array([1, 2, 3, 4])
# print(a)
# print(a+2)
# print(a-2)
# print(a/2)
# b = np.array([1,0,1,0])
# print(a+b)
# print(a ** 2)
# print(np.sin(a))

# Linear Algebra
# a = np.ones((2,3))
# print(a)
#
# b = np.full((3,2), 2)
# print(b)
#
# print("\n")
# print(np.matmul(a,b))
#
# Statistics

# a  = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.min(a))
# print(np.max(a))
# print(np.sum(a))

# before = np.array([[1, 2, 3, 4], [5, 6,7,8]])
# print(before)
#
# after = before.reshape((4,2))
# print(after)
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])
#
# print(np.vstack([v1, v2]))

filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata > 50)