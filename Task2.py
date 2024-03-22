import numpy as np

A1 = np.random.randint(0 , 101 , 8)

A2 = np.random.randint(0 , 101 ,(4,5))

A3 = np.random.randint(0 , 101 ,(3,4,4))

print(A1 , "\n\n\n===============================")

print(A2 , "\n\n\n===============================")

print(A3 , "\n\n\n===============================")

print("Third element of one dimensional array:\n" , A1[2] , "\n\n\n================")

print("Element at position [2,3] of two dimensional array:\n" , A2[2,3] , "\n\n\n================")

print("2x2 left upper corner of two dimensional array:\n" , A2[0:2,0:2] , "\n\n\n================")

print("iterating in three dimensional array:\n")

for i in range(len(A3)):
    print(A3[i], "\n\n========")      