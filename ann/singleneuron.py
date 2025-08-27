import torch
import torch.nn.functional as F

x= torch.tensor([2.0, -1.0, 3.0])
w= torch.tensor([0.4, 0.1, -0.2])
b=0.5

z= torch.dot(x,w)+b
print("Weighted sum z:", z)

sigmoid_output= torch.sigmoid(z)
print("Sigmoid activation output:", sigmoid_output)
a= F.relu(z)
print("ReLU activation output:", a)
