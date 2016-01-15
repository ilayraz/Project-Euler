from math import sqrt
from itertools import count


def myIsPrime(num):
    # My version
    if num < 2:
        return False
    if num == 2:
        return True
    if not num & 1:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if not num % i:
            return False
    return True


def isPrime(num):
    """ improved version """
    if num < 2:
        return False
    if num < 4:
        return True
    if not num & 1:
        return False
    if num < 10:
        return True
    if not num % 3:
        return False
    for i in range(5, int(sqrt(num)) + 1, 6):
        if not num % i:
            return False
        if not num % (i+2):
            return False
    return True


def primeGen():
    yield 2

    for i in count(3, step=2):
        if isPrime(i):
            yield i


def main(n):
    """ nth prime number """
    if n == 0:
        return

    for i, k in enumerate(primeGen()):
        if i == n - 1:
            return k

