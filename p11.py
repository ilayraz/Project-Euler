from functools import reduce
from operator import mul

text = list(map(lambda x: x.split(), open("p11.txt").read().split("\n")))[:-1]
text = [list(map(int, x)) for x in text]

maxR = max((reduce(mul, row[x:x + 4])
            for row in text for x in range(len(row) - 3)))
maxC = max((reduce(mul, (text[y + i][x] for i in range(4)))
            for x in range(len(text[0])) for y in range(len(text) - 3)))
maxDF = max((((reduce(mul, (text[y + i][x + i] for i in range(4)))
               for x in range(len(text[0]) - 3)
               for y in range(len(text) - 3)))))
maxDB = max((reduce(mul, (text[y + i][x - i] for i in range(4)))
          for x in range(3, len(text[0])) for y in range(len(text) - 3)))

print(max(maxR, maxC, maxDF, maxDB))
