import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points in 3D space
x, y, z = np.meshgrid(np.linspace(-1, 1, 10), 
                      np.linspace(-1, 1, 10), 
                      np.linspace(-1, 1, 10))

# Define the vector field H(x, y, z) = [-x, -y, -z]
u = -x
v = -y
w = -z

# Plotting the vector field using quiver
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector Field: H(x, y, z) = [-x, -y, -z]')

plt.show()
