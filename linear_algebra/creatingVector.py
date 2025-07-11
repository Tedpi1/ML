import numpy as np
x=np.array([20,4,5])
print(x)
x_s=x.shape
size_x=len(x)
print("size",size_x)
print("shape",x_s)
y=np.array([30,6,7])
sum_x=x+y
pyrid_sum=sum_x.tolist()
print("sum",pyrid_sum)