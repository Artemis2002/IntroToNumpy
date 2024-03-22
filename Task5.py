import numpy as np

A = np.random.randint(0,11,(3,4))

print("matrix A:\n" , A , "\n\n========================")

print("Mean of matrix A :\n" , np.mean(A) , "\n\n=========================")

print("mediant of matrix A :\n" , np.median(A) , "\n\n=========================")

print("variance of matrix A :\n" , np.var(A) , "\n\n=========================")

print("standard deviation of matrix A :\n" , np.std(A), "\n\n=========================")

####################################

B1 = np.random.randint(0,11,5)

B2 = np.random.randint(0,11,5)

print("matrix B1:\n" , B1 , "\n\n============")
print("matrix B2:\n" , B2 , "\n\n============")

X = np.corrcoef(B1,B2)

print("Coefficient Between B1 and B2:\n" , X)