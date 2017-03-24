import datetime

day = datetime.timedelta(days=1)
start = datetime.datetime(1901, 1, 1)
end = datetime.datetime(2000, 12, 31)
count = 0

while start <= end:
    if start.day == 1 and start.weekday() == 6:
        count += 1
    start += day

print(count)
