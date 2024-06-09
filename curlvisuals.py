import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of points in 3D space
x, y, z = np.meshgrid(np.linspace(-2, 2, 10), 
                      np.linspace(-2, 2, 10), 
                      np.linspace(-2, 2, 10))

# Define the vector field F(x, y, z) = [xy + z, yz + x, zx + y]
u = x * y + z
v = y * z + x
w = z * x + y

# Compute the divergence: ∇·F = x + y + z
divergence = x + y + z

# Compute the curl: ∇×F = [1 - y, 1 - z, 1 - x]
curl_u = 1 - y
curl_v = 1 - z
curl_w = 1 - x

# Plotting the vector field
fig = plt.figure(figsize=(18, 6))

# Vector Field
ax1 = fig.add_subplot(131, projection='3d')
ax1.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Vector Field: F(x, y, z)')

# Divergence
ax2 = fig.add_subplot(132, projection='3d')
div_scatter = ax2.scatter(x, y, z, c=divergence, cmap='coolwarm')
fig.colorbar(div_scatter, ax=ax2, shrink=0.5, aspect=5)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Divergence of F(x, y, z)')

# Curl
ax3 = fig.add_subplot(133, projection='3d')
ax3.quiver(x, y, z, curl_u, curl_v, curl_w, length=0.1, normalize=True)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title('Curl of F(x, y, z)')

plt.show()
