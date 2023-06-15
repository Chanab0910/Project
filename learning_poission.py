from numpy import random

var = 0.0128 * 90

for i in range(10):
    x = random.poisson(lam=var)
    print(x)