from math import sqrt


def isPrime(num):
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


def lowestPrimeDivisor(num):
    if not num & 1:
        return 2
    for i in range(3, int(sqrt(num)) + 1, 2):
        if isPrime(i) and not num % i:
            return i
    return None


def main(num):
    while(not isPrime(num)):
        num //= lowestPrimeDivisor(num)
    return num
