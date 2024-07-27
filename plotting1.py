import numpy as np
import matplotlib.pyplot as plt

# Create values for y
y = np.linspace(0, 2, 400)
# Calculate x values on the parabola
x_parabola = y**2

# Plot the region
plt.figure(figsize=(8,6))

# Plot the parabola x = y^2
plt.plot(x_parabola, y, label='$x = y^2$')

# Plot the vertical line x = 4
plt.plot([4, 4], [0, 2], label='$x = 4$', color='orange')

# Fill the region of integration
plt.fill_betweenx(y, x_parabola, 4, alpha=0.3, color='grey')

# Labels and Title
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Region of Integration for $\int_{0}^{2} \int_{y^2}^{4} e^{y/\\sqrt{x}} \, dx \, dy$')
plt.legend()
plt.grid(True)
plt.show()
