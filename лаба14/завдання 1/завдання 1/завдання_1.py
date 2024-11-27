import matplotlib.pyplot as plt
import numpy as np

# Define the function and the range
x = np.linspace(0.1, 5, 500)  # Start from 0.1 to avoid division by zero
y = 10 * np.cos(x**2) / x**2

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label=r'$y(x) = \frac{10 \cos(x^2)}{x^2}$')

# Add labels, title, and legend
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Graph of the function $y(x) = \\frac{10 \\cos(x^2)}{x^2}$', fontsize=16)
plt.legend(fontsize=12)
plt.grid(True)

# Show the plot
plt.show()

