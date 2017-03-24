import library
import itertools
import functools
import operator


def triagGen():
    sum = 0
    for i in itertools.count(1):
        sum += i
        yield sum


def firstPass():
    for num in triagGen():
        factors = functools.reduce(operator.mul,
                                   (x + 1
                                    for k, x in library.primeFactor(num)), 1)
        if factors > 500:
            print(num)
            break


firstPass()
