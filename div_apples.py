import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of points in 3D space
x, y, z = np.meshgrid(np.linspace(-1, 1, 10), 
                      np.linspace(-1, 1, 10), 
                      np.linspace(-1, 1, 10))

# Define the vector field G(x, y, z) = [x^2y + yz, y^2z + zx, z^2x + xy]
u = x**2 * y + y * z
v = y**2 * z + z * x
w = z**2 * x + x * y

# Plotting the vector field using quiver
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(121, projection='3d')
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector Field: G(x, y, z)')

# Compute the divergence
divergence = 2 * x * y + 2 * y * z + 2 * z * x

# Plotting the divergence using a scatter plot with color map
ax2 = fig.add_subplot(122, projection='3d')
sc = ax2.scatter(x, y, z, c=divergence, cmap='coolwarm', marker='o')

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Divergence of G(x, y, z)')
fig.colorbar(sc, ax=ax2, shrink=0.5, aspect=5)

plt.show()
