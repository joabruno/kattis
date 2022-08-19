cases = int(input())
for c in range(cases):
    case = input().split()
    avg = sum([int(x) for x in case[1:]])/int(case[0])
    above_avg = sum([1 if int(x) > avg else 0 for x in case[1:]])/int(case[0])*100
    percent = round(above_avg, 3)
    print(f'{percent:.3f}'+"%")