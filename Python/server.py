tasks, time = map(int, input().split())

task = list(map(int, input().split()))
time_used = 0
for i, t in enumerate(task):
    time_used += t
    if time_used > time:
        print(i)
        break
if time >= time_used:
    print(len(task))