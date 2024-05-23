# Using numpy.random.rand()
import numpy as np
import matplotlib.pyplot as plt

num=10000
ran = np.random.rand(num)

u = np.ones(num)
v = np.linspace(0, 1, num)

plt.hist(ran, bins=20, density=True, label = 'Histogram')
plt.plot(v, u, label = 'Uniform Distribution')
plt.xlabel('Random number')
plt.title('Random numbers using numpy.random.rand()')
plt.ylabel('Frequency')
plt.legend()
plt.show()

