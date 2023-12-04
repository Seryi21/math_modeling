gravitational_constant = 9.81
weight = 10
speed = 10
hight = 10

def energy(weight, speed, hight, gravitational_constant):
    en = (weight * gravitational_constant * hight) + ((weight * speed**2) / 2)
    return en

print(energy(weight, speed, hight, gravitational_constant))