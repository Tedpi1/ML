import numpy as np
import torch

x = np.array([25, 2, 5])
y = np.array([0, 1, 2])
print("Array of x is:", x)
print("Array of y is:", y)

xy_dot = np.dot(x, y)
print("Dot product of x and y is:", xy_dot)

x_pt = torch.tensor([25, 2, 5], dtype=torch.float32)
y_pt = torch.tensor([0, 1, 2], dtype=torch.float32)

xypt_dot = torch.dot(x_pt, y_pt)
print("Torch Dot function Result is:", xypt_dot.item())
