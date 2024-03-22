import numpy as np
import matplotlib.pyplot as plt
X = np.random.randint(0,11,2)
Y = np.random.randint(0,11,2)

Z = np.polyfit(X,Y,2)

print("Resault of Polynomial Fitting:\n" , Z , "\n\n================================")

plt.plot(X,Y)
plt.show()
