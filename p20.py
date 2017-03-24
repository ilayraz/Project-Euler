from operator import mul
from functools import reduce

num = 100
print(sum(int(i) for i in str(reduce(mul, range(1, num + 1), 1))))


