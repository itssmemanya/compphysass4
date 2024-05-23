import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.sqrt(2 / np.pi)) * np.exp(- x**2 / 2)

n = 1000
x = np.linspace(0, 5, n)
y = f(x)
r = np.random.rand(n) * 0.8
ran = []
t = []

for i in range(n):
    if r[i] <= y[i]:
        ran.append(r[i])
        t.append(x[i])
        
plt.scatter(x, r, label = 'Rejected numbers', color = 'r')
plt.scatter(t, ran, label = 'Accepted numbers', color = 'g')
plt.plot(x, y, label = 'Given Distribution', color = 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

plt.plot(y, x, label = 'Given Distribution', color = 'b')
plt.hist(ran, bins = 10, density = True, color = 'y')
plt.xlabel('Values in Distribution')
plt.ylabel('Frequency (Normalized to bin)')
plt.title('Density Histogram')
plt.show()
