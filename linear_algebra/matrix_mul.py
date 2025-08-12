import numpy as np
import torch
import tensorflow as tf

A=np.array([[1, 2], [3, 4], [5, 6]])
B=np.array([[1,9],[2,0]])

AB=np.dot(A, B)
print("Matrix multiplication using Numpy:\n", AB)

A_pt=torch.tensor([[1, 2], [3, 4], [5, 6]])
B_pt=torch.from_numpy(B)
AB_pt=torch.matmul(A_pt, B_pt)
print("Matrix multiplication using PyTorch:\n", AB_pt)

A_tf=tf.Variable([[1, 2], [3, 4], [5, 6]])
B_tf=tf.convert_to_tensor(B, dtype=tf.int32)
AB_tf=tf.matmul(A_tf, B_tf)
print("Matrix multiplication using TensorFlow:\n", AB_tf.numpy())