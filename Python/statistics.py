cases = 1
while True:
    try:
        case = [int(i) for i in input().split()]
    except:
        break
    case = case[1:]
    print("Case %d: %d %d %d" % (cases, min(case), max(case), max(case)-min(case)))
    cases += 1