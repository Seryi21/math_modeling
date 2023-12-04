sp = [1,2,3,4,5,6,7,8,9,10]
def srednee(a):
    quantity = len(a)
    proizvedenie = 1
    for i in a:
        proizvedenie *= i
    return proizvedenie

print(srednee(sp))
