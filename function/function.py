'''
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
'''

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        a, b = b, a + b
        n = n + 1
    return b

print (fib(5))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))
print(fact(200))

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print (L[0:3])

L = ['Hello', 'World', 'IBM', 'Apple']
for s in L:
    print(s.lower())

f = abs
print(f(-3))

def add(x, y, f):
    return f(x) + f(y)

print(add(3, -4, f))
