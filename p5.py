# Only needs to compute lcm of 11-20.

from functools import reduce


def gcd(a, b):
    """ Euclidean algorithm """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


def lcmm(*args):
    """ lcm for args """
    return reduce(lcm, args)

lcmm(*range(11, 21))
