import numpy as np 

A = np.array([[1,2,3,4,5,6,7] ,[8,9,10,11,12,13,14]] , dtype="float32")

print("A*2: ", A*2 , "\n\n=====================")

print("A/2: ", A/2 , "\n\n====================")

print("A+1: ", A+1 , "\n\n====================")

print("A-1: ", A-1 , "\n\n====================")


###################################

B = np.array([[15] ,[14]])

for i in range(len(A[1])):
    for j in range(len(A)):
        A[j,i] = A[j,i] + B[j,0]
        
print("vector adding B to A:\n\n" , A)

####################################

C = np.array([[1,2,3,4] , [5,6,7,8] , [9,10,11,12]])

C2 = np.reshape(C , (2 , 6))

C1 = np.reshape(C , (1 , 12))          
    
print("Three dimensional matrix C:\n" , C , "\n\n================================")

print("Three dimensional matrix C reshaped to two dimensional matrix:\n" , C2 , "\n\n================================")

print("Three dimensional matrix C flattered to one dimensional matrix:\n" , C1 , "\n\n================================")
