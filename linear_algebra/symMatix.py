import numpy as np

# Create a symmetric matrix
X=np.array([[4,5,2],[5,3,1],[2,1,6]])
print("Original Matrix:\n", X)

X_t=X.T
print("Transpose of Matrix:\n", X_t)

X == X_t