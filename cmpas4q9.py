import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.where(np.logical_and(x>3, x<7), 0.25, 0)

n = 1000
theta = [6.5]
alltheta = [6.5]
it = [0]
for i in range(n):
    theta_prime = np.random.standard_normal() + theta[-1]
    r = np.random.rand()
    it.append(i)
    alltheta.append(theta_prime)
    if f(theta_prime) / f(theta[-1]) > r:
        theta.append(theta_prime)
    else :
        theta.append(theta[-1])

plt.hist(theta, bins = 20, density = True, color = 'g', label = 'Density Histogram')
x = np.linspace(0, 10, 100)
y = f(x)

plt.plot(x, y, color = 'r', label = 'Given Distribution')
plt.legend()
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Markov Chain Monte Carlo using Metropolis Algorithm')
plt.show()

plt.plot(it, theta, linestyle = '-', color = 'blue', label = 'Markov Chain')
plt.scatter(it, alltheta, color = 'orange', label = 'Rejected points')
plt.scatter(it, theta, color = 'b', label = 'accepted points')
plt.title('Markov Chain visualised')
plt.xlabel('Iteration')
plt.ylabel('Value using MCMC')
plt.xlim(0,200)
plt.legend()
plt.show()
