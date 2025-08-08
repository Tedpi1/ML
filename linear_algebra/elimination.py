import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

y1=-5 + (2*x)/3
y2=(7-2*x)/5

fig, ax= plt.subplots()
plt.xlabel('x')  # label for x-axis
plt.ylabel('y')  # label for y-axis
plt.title('Graph of Two Linear Equations Using elimination')  # title of the plot
# add x and y axis
plt.axvline(x=0, color='black')  # vertical line at x=0
plt.axhline(y=0, color='black')  # horizontal line at y=0

ax.set_xlim([-2, 10])  # set x-axis limits
ax.set_ylim([-6, 4])  # set y-axis limits

ax.plot(x, y1, c='green')  # plot first line in green
ax.plot(x, y2, c='brown')  # plot second line in brown

plt.axvline(x=6, color='purple', linestyle='--')  # vertical line at x=3
_ = plt.axhline(y=-1, color='purple', linestyle='--')


plt.show()  # display the plot