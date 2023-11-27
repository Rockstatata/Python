import matplotlib.pyplot as plt
import numpy as np

# Define the parameters a and p
a = 1
p = 1

# Generate values of t from 0 to 2*pi with a small increment
t = np.linspace(0, 2*np.pi, 1000)

# Calculate x and y coordinates using the given equations
x = a * np.sin(p * t)
y = 2 * a * np.sin(2 * p * t)

# Plot the Lissajous figure
plt.plot(x, y)
plt.title('Lissajous Figure: x = asin(pt), y = 2asin(2pt)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
