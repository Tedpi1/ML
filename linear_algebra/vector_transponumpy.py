import numpy as np
import torch
import tensorflow as tf
X=np.array([[24,4],[12,4],[2,3]])
print("Numpy array:\n", X)
# transpose of 
x_t=X.T
print("Transpose of X:\n", x_t)
# transpose using tensorflow
x_tf= tf.transpose(X)
print("Transpose of X using tensorflow:\n", x_tf)
# transpose using torch
x_torch= torch.tensor(X).t()
print("Transpose of X using torch:\n", x_torch)