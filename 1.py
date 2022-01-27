from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def Fibonacci(inicio, final):
    n = 0
    cur = F(n)
    while cur <= final:
        if inicio <= cur:
            print(cur)
        n += 1
        cur = F(n)
Fibonacci(1000,10000)