import numpy as np

s = np.random.randn(3073, 10)
x = np.random.randn(10, 1000)

def dotmulti(a, b):
    w = np.dot(a, b)
    return w

e = dotmulti(s, x)
print e