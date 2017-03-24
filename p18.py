nums = [[int(k) for k in i.split()]
        for i in open("p18.txt").read().splitlines()]
mems = [[0] * i for i in range(1, len(nums) + 1)]


def pval(x, y):
    if not (0 <= y < len(nums) and 0 <= x < len(nums[y])):
        return 0

    if mems[y][x] == 0:
        mems[y][x] = nums[y][x] + max(pval(x, y + 1), pval(x + 1, y + 1))
    return mems[y][x]


print(pval(0, 0))
