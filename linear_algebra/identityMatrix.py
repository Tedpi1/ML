import torch

A=torch.tensor([[1,0,0],[0,1,0],[0,0,1]])
print("The Original Matrix:\n", A)

x_pt=torch.tensor([5,6,7])
Ax_pt=torch.matmul(A, x_pt)
print("Result of multiplying by Identity Matrix:\n", Ax_pt)