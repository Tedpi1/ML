import numpy as np
X=np.array([[1, 2], [3, 4],[5, 6]])
print("Matrix X:\n", X)
print("Shape of X:", X.shape)
print("Squared L2 norm of X:", np.sum(X**2))
print("Size of X:", X.size)
print("select left column", X[:, 0])
print("Select middle row", X[1, :])
print("Select the last Row", X[-1, :])