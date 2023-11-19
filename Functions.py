from Number import *

def factorial(x):
    assert x >= 0
    result = Number(1)
    for i in range(2, x + 1):
        result *= i
    return result

def double_factorial(x):
    assert x >= 0
    result = Number(1)
    for i in range(2 + x % 2, x + 1, 2):
        result *= i
    return result

def C(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)

def A(n, k):
    return factorial(n) / factorial(k)