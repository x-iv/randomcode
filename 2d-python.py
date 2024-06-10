import numpy as np
import matplotlib.pyplot as plt

# Define the vector field F = [-y, x]
def vector_field(x, y):
    F1 = -y
    F2 = x
    return F1, F2

# Create a grid of points
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)
U, V = vector_field(X, Y)

# Calculate the scalar curl of the vector field at each point
curl = np.zeros_like(X)
for i in range(len(x)):
    for j in range(len(y)):
        # Partial derivatives
        dF2_dx = 1  # partial derivative of x with respect to x is 1
        dF1_dy = -1  # partial derivative of -y with respect to y is -1
        curl[i, j] = dF2_dx - dF1_dy

# Plot the vector field
plt.figure(figsize=(12, 8))

# Quiver plot of the vector field
plt.quiver(X, Y, U, V, color='b')

# Contour plot of the scalar curl
plt.contourf(X, Y, curl, alpha=0.5, cmap='coolwarm')
plt.colorbar(label='Curl (scalar)')

plt.title('Vector Field F = [-y, x] with Scalar Curl')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)
plt.grid(True)
plt.show()
