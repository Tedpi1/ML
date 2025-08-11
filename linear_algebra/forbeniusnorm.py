import numpy as np 
import torch
import tensorflow as tf

X=np.array([[1,2],[3,4]])
norm_x=np.linalg.norm(X)
print("Forbenius norm of X using Numpy",norm_x)

X=torch.tensor([[1,2],[3,4.]])
norm_xt=torch.norm(X)
print("Forbenius norm of X using Torch",norm_xt)

x_tf=tf.Variable([[1,2],[3,4.]])
norm_xtf=tf.norm(x_tf)
print("Forbenius norm of X using TensorFlow",norm_xtf)

