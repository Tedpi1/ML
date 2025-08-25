import torch
import matplotlib.pyplot as plt

# Set seed for reproducibility
_ = torch.manual_seed(42)

# Set number of neurons
n_input = 784   # Flattened 28x28 image
n_dense = 256   # Number of neurons in hidden layer

# Simulate an "input image" with a vector tensor x
x = torch.randn(n_input)  # Samples from normal distribution (mean=0, std=1)

# Print details
x_shape = x.shape
print("Input tensor shape:", x_shape)

x_size = torch.Size([n_input])
print("Input tensor size:", x_size)

zero_x = x[0:6]
print("First 6 values of input tensor:", zero_x)

# Plot histogram of input values
plt.hist(x, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of Input Tensor Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, alpha=0.3)
plt.show()
