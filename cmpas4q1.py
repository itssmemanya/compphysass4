# Linear Congruential Random Number Generator
# Developped by Derrick Lehmer
import numpy as np
import matplotlib.pyplot as plt
def next_num(x, a, c, m):
    return (a*x + c) % m

print(' Linear Congruential Random number generator ')
x = int(input(' Enter seed : '))
a = int(input(' Enter a : '))
c = int(input(' Enter c : '))
m = int(input(' Enter m : '))
num = 10000
ran = [x]
for i in range(num):
    ran.append(next_num(ran[-1], a, c, m))

y = max(ran)
ran = [ x/y for x in (ran)]

u = np.ones(num)
v = np.linspace(0, 1, num)

plt.hist(ran, bins=20, density=True, label = 'Histogram')
plt.plot(v, u, label = 'Uniform Distribution')
plt.xlabel('Random number')
plt.title('Random numbers using Linear Congruential method')
plt.ylabel('Frequency')
plt.legend()
plt.show()

