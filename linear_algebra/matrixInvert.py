import numpy as np

X=np.array([[4,2],[-5,-3]])
print("Original Matrix:\n", X)
Xinv=np.linalg.inv(X)
print("Inverse of Matrix:\n", Xinv)
y=np.array([4,-7])
w=np.dot(Xinv,y)
print("The Final weights are:\n", w)