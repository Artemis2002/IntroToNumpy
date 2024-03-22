import numpy as np

A = np.array([[1, 2, 3] , [4, 5, 6] , [7, 8, 9]])

B = np.array([[10] , [11] , [12]])

C = np.dot(A, B)

print("Dot product of A and B =\n" , C )


####################################

Z = np.random.randint(0 ,11 ,(3,3))

deter = np.linalg.det(Z)

print("matrix 3x3 of Z:\n" , Z , "\n\n================================")

print("determinant of matrix Z =\n" , deter , "\n\n================================")

invers = np.linalg.inv(Z)
print("Invers of matrix Z =\n" , invers , "\n\n================================")


evalue , evector = np.linalg.eig(Z)

print("evalue of matrix Z =\n" , evalue , "\n\n================================")

print("evector of matrix Z =\n" , evector , "\n\n================================")

