""" library of generic functions to import """

import math


def gcd(a, b):
    """ Euclidean algorithm. Can also use math.gcd """
    while b:
        a, b = b, a % b
    return a


def primeGen():
    """ infinite prime generator. http://stackoverflow.com/a/19391111 """
    import itertools
    yield from (2, 3, 5, 7)
    D = {}
    ps = primeGen()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p * p
    for i in itertools.count(9, 2):
        if i in D:  # composite
            step = D.pop(i)
        elif i < psq:  # prime
            yield i
            continue
        else:  # composite, = p*p
            assert i == psq
            step = 2 * p
            p = next(ps)
            psq = p * p
        i += step
        while i in D:
            i += step
        D[i] = step


def isPrime(num):
    """ checks if num is a prime """
    for i in primeGen():
        if num == i:
            return True
        elif i > num:
            return False


def ithPrime(num):
    """ gets the nth prime """
    for i, p in enumerate(primeGen()):
        if i == num:
            return p


def factor(num):
    for i in range(1, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            div = num // i
            yield i
            if i != div:
                yield div


def primeFactor(num):
    """ prim factorizes num """
    for i in primeGen():
        if i > num:
            break
        count = 0
        while num % i == 0:
            count += 1
            num //= i
        if count:
            yield i, count


def pyGen():
    """ generates Pythagorean triplets. Uses Euclid's formula """
    import itertools
    for m in itertools.count(2):
        for n in range(1, m):
            yield (m**2 - n**2, 2 * m * n, m**2 + n**2)
