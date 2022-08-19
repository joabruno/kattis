while True:
    case = input()
    if case == "-1":
        break
    l = []
    prev = 0
    miles = 0
    for _ in range(int(case)):
        speed, hour = input().split()
        miles += int(speed)*(int(hour)-prev)
        prev = int(hour)
    print("{} miles".format(miles))