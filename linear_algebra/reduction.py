import  numpy as np
import torch
import tensorflow as tf
X=np.array([[25, 2], [5, 26], [3, 7]])
print("The sum in Numpy is ", X.sum())
x_pt=torch.tensor(X)
print("The sum in Pytorch is ", x_pt.sum())
x_tf=tf.constant(X)
print("The sum in Tensorflow is ", tf.reduce_sum(x_tf))

# specifc axis using numpy
print("Suming all Rows", X.sum(axis=0))
print("Suming all Columns", X.sum(axis=1))

# specifi axis using pytorch
print("suming all Rows in Pytorch", x_pt.sum(axis=0))
print("suming all Columns in Pytorch", x_pt.sum(axis=1))

# Specific axis using tensorflow
print("Suming all Rows in Tensorflow", tf.reduce_sum(x_tf, axis=0))
print("Suming All columns",tf.reduce_sum(x_tf, axis=1))
