import numpy as np

x=np.array([25,2,5])
norm=(25**2+2**2+5**2)**0.5
print("L2 norm of x:", norm)

norm_x=np.linalg.norm(x)
print("L2 norm of x using numpy:", norm_x)