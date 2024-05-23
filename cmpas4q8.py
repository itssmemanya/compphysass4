import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.where(x**2 + y**2 <= 1, 1, 0)

n = 100000
A = 4 # Area of the Box
# Radius = 1 Thus area of square surrounding circle is diameter^2
x_ran = np.random.rand(n)
y_ran = np.random.rand(n)

# Number of points falling in the integral
k = np.sum(f(x_ran, y_ran))

#Integration by Monte Carlo Method
I = k * A / n

print(' The Area of the circle through Monte Carlo integration is ', I)
