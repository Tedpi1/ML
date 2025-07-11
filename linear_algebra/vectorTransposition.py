import creatingVector
import numpy as np
x=creatingVector.x
x_t=x.T
print("x_t", x_t)
x_sT=x_t.shape
print("shape of x_t", x_sT)
y=np.array([[30,6,7]])
print("y", y)
y_s=y.shape
print("shape of y", y_s)
y_t=y.T
print("y_t", y_t)
y_sT=y_t.shape
print("shape of y_t", y_sT)