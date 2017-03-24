nums  = open("p13.txt").readlines()
sum = 0
for num in nums:
    sum += int(num)
print(str(sum)[:10])
