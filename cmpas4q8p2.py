import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.where((x**2).sum(axis = 1) <= 1, 1, 0)

n = 10000000
d = 10 # 10 dimensional sphere
A = 2**d # Volume of the Box
# Radius = 1 Thus volume of box surrounding d-dim sphere is diameter^d
x_ran = np.random.rand(n,d)

# Number of points falling in the integral
k = np.sum(f(x_ran))

#Integration by Monte Carlo Method
I = k * A / n

print(' Volume of the 10-dimensional sphere through MC integration is ', I)
