seeds = int(input())
growing_time = sorted([int(i) for i in input().split()])
growing_time.reverse()
day = 1
for i, g in enumerate(growing_time):
    if (g + i+1) > day:
        day = (g + i+1)
    
print(day+1)


