from lab_3_task_4 import table as t
import numpy as np

#sp = []
r = int(input())
rr = int(input())

n = len(t)
m = len(t[0])

#for j in range(n):
    #sp.append(t[j, r])

for i in range (n):
    t[i, r], t[i, rr] = t[i, rr], t[i, r]
    #t[i, r] = t[i, rr]
    #t[i, rr] = sp[i]

print(t)
