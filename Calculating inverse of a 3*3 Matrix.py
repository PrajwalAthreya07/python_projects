#import the numerical python(numpy) package
import numpy as np

#creating a 3*3 matrix array
print("Given Matrix is")
matrix = np.array([[2,4,-8],[3,-7,9],[5,7,1]])

#printing the matrix array
print(matrix)
print()

#inverse matrix
print("inverse of the given matrix is")
invmat = np.linalg.inv(matrix)
print(invmat)
print()

#to check if the inverse matrix obtained is correct,we just need to multiply our matrix array and inverse matrix to get identity matrix(3*3) as the output.
print("identity matrix obtained when matrix is multiplied with its inverse")
a = np.matmul(matrix , invmat)
print(a)
