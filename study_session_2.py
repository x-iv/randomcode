import numpy as np
import matplotlib.pyplot as plt

# Define the function f(t)
def f(t):
    return np.where(t <= -1, (t + 2)**2, np.where(t <= 1, t**2, (t - 2)**2))

# Define the points to be marked
points = np.array([-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2])
values = f(points)

# Create the plot
t = np.linspace(-2, 2, 400)
ft = f(t)

plt.figure(figsize=(10, 6))
plt.plot(t, ft, label='$f(t) = t^2$', color='blue')
plt.scatter(points, values, color='red', zorder=5)
for point, value in zip(points, values):
    plt.text(point, value, f'({point}, {value:.2f})', fontsize=9, ha='right')

# Mark the points
plt.scatter(points, values, color='red')

# Set plot labels and title
plt.xlabel('$t$')
plt.ylabel('$f(t)$')
plt.title('Graph of $f(t) = t^2$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
