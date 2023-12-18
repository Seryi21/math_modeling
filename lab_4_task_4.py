import numpy as np

def function(a, b, N):
    table = np.arange(a, b+1, N)
    y = table**2
    return y
print(function(1, 5, 0.01))
    
