from lab_3_task_1 import acceleration_of_free_fall as g
import numpy as np

vx0 = 5
vy0 = 10
x0 = 0
y0 = 0

time = np.arange(0, 6, 0.1)
table = np.zeros((len(time), 3))

x = x0 + vx0*time
y = y0 + vy0*time - (g * time**2)/2

for i in range(len(time)):
    table[i, 0] = time[i]
    table[i, 1] = x[i]
    table[i, 2] = y[i]

print(table)




 
