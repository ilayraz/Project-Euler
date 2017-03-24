import library
from operator import mul
from functools import reduce


def sumDiv(n):
    return reduce(mul, ((a**(b + 1) - 1) // (a - 1)
                        for a, b in library.primeFactor(n)), 1) - n


arr = []

for i in range(10000):
    arr.append(sumDiv(i))

sum = 0

for i in range(3, len(arr)):
    try:
        if arr[arr[i]] == i and i != arr[i]:
            sum += i
    except IndexError:
        pass

print(sum)
