import numpy as np
import matplotlib.pyplot as plt

n = 5000

# Box-Muller transform
u1 = np.random.rand(n)
u2 = np.random.rand(n)
z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)

gaussian_numbers = np.concatenate((z0, z1))[:n]

mean = 0
var = 1
x = np.linspace(-4, 4, 1000)
gauss_pdf = (1/(np.sqrt(2 * np.pi * var))) * np.exp((-0.5 / var) * (x - mean)**2)

plt.hist(gaussian_numbers, bins=50, density=True, color='g')
plt.plot(x, gauss_pdf, linewidth=2, color='r')
plt.title('Histogram of Gaussian Numbers and Gaussian PDF')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
