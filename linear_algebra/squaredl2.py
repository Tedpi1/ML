import numpy as np

x = np.array([20, 4, 5])
sql2Norm=(20**2+4**2+5**2)
print("Squared L2 norm of x:", sql2Norm)
dotsqNorm = np.dot(x, x)
print("Squared L2 norm of x using numpy:", dotsqNorm)