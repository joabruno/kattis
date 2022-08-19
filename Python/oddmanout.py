for case in range(int(input())):
    numbers = int(input())
    numbers_ = input().split()
    numlist = sorted([x for x in numbers_])

    for i in range(numbers):
        
        if numlist[i] not in numlist[0:i] + numlist[i+1:] and i % 2 == 0:
            print("Case #{0}: {1}".format(case+1, numlist[i]))
        