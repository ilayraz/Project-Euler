from library import pyGen
from operator import mul
from functools import reduce

total = 65466828 #1000

for trip in pyGen():
    if sum(trip) == total:
        print(trip, reduce(mul, trip))
        break
