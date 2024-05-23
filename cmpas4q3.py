# Time for each code in Q1 and Q2
import numpy as np
import matplotlib.pyplot as plt
import time

num=10000000
# Increased number of points because time elapsed was too small

# Linear Congruential Random Number Generator
def next_num(x, a, c, m):
    return (a*x + c) % m
print(' Linear Congruential Random number generator ')
x = int(input(' Enter seed : '))
a = int(input(' Enter a : '))
c = int(input(' Enter c : '))
m = int(input(' Enter m : '))
ran1 = [x]
time1i = time.time_ns()
for i in range(num):
    ran1.append(next_num(ran1[-1], a, c, m))
y = max(ran1)
ran1 = [ x/y for x in (ran1)]
time1f = time.time_ns()
time1 = time1f - time1i
print(' Time taken by Linear Congruential method is ', time1 * 10**-9, ' s')

# Using numpy.random.rand()
time2i = time.time_ns()
ran2 = np.random.rand(num)
time2f = time.time_ns()
time2 = time2f - time2i
print(' Time taken by numpy.random.rand() is ', time2 * 10**-9, ' s')

# Clearly time taken by numpy is much smalleras compared to my code
