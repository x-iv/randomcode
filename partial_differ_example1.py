import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function and its partial derivatives
def f(x, y):
    return x**2 * y + 3 * x * y + 5

def partial_f_x(x, y):
    return 2 * x * y + 3 * y

def partial_f_y(x, y):
    return x**2 + 3 * x

# Generate a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Calculate the function and its partial derivatives on the grid
z = f(x, y)
z_x = partial_f_x(x, y)
z_y = partial_f_y(x, y)

# Create a 3D plot for the original function
fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(x, y, z, cmap='viridis')
ax1.set_title('Original Function $f(x, y) = x^2 y + 3xy + 5$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

# Create a 3D plot for the partial derivative with respect to x
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(x, y, z_x, cmap='plasma')
ax2.set_title('Partial Derivative with respect to x: $\\frac{\\partial f}{\\partial x}$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('$\\frac{\\partial f}{\\partial x}$')

# Create a 3D plot for the partial derivative with respect to y
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(x, y, z_y, cmap='inferno')
ax3.set_title('Partial Derivative with respect to y: $\\frac{\\partial f}{\\partial y}$')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('$\\frac{\\partial f}{\\partial y}$')

plt.tight_layout()
plt.show()
