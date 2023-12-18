def degree(a, n):
    for i in range(n-1):
        a *= a
    return a
print(degree(2, 10))