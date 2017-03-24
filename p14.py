maxnum = 10**6
collat = dict()
collat[1] = 0

def getCollatz():
    maxim = maxcoll = 0
    for i in range(1, maxnum):
        curr = collatz(i)
        if curr > maxcoll:
            maxcoll = curr
            maxim = i
    return maxim

def collatz(curr):
    if curr in collat:
        return collat[curr]
    else:
        collat[curr] = 1 + collatz((3 * curr + 1) if curr & 1 else curr // 2)
        return collat[curr]


print(getCollatz())

