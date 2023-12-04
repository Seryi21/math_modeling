import numpy as np

n = int(input())
m = int(input())
table = np.zeros((n, m))

for i in range(n):
    for j in range(m):
        A = np.sin(n*(i+1) + m*(j + 1))
        if A < 0:
            table[i, j] = 0
        table[i, j] = A
print(table)
        
        
        
