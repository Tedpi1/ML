import torch
import torch.nn as nn
import torch.nn.functional as F

# Define a small neural network class
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 128) #Layer 1 (784 inputs, 128 outputs)
        self.fc2 = nn.Linear(128, 64)  #Layer 2 (128 inputs, 64 outputs)
        self.fc3 = nn.Linear(64, 10)   #Layer 3 (64 inputs, 10 outputs)

    def forward(self, x):
        x = F.relu(self.fc1(x)) #Layer 1 activation
        x = F.relu(self.fc2(x)) #Layer 2 activation
        x = F.softmax(self.fc3(x), dim=1) #Layer 3 activation
        return x

# Instantiate the neural network
x= torch.randn(1, 784) # Example input tensor
model = SimpleNN()
output = model(x)

print("Neural Network output:", output)
print("Sum of output probabilities:", torch.sum(output).item())
        