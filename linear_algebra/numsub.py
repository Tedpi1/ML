import numpy as np
# x+y=6, 2x+3y=16
a=np.array([[1,1],[2,3]])
b=np.array([6,16])
x=np.linalg.solve(a,b)
print(x)
