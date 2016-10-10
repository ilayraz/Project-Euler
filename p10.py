import library

k = total = 0
gen = library.primeGen()

while k < 2000000:
    total += k
    k = next(gen)

print(total)
