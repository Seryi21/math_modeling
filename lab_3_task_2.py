from lab_3_task_1 import acceleration_of_free_fall as g 
import numpy as np

h = 100
alpha = np.pi/3
beta = 30

speed = np.sqrt((g*h * (np.tan(beta))**2) / (2 * np.cos(alpha)**2 * (1 - np.tan(beta) * np.tan(alpha))))
print(speed)