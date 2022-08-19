while True:
    frac = input()
    if frac == "0 0":
        break
    n1, n2 = [int(x) for x in frac.split()]
    print(n1//n2,n1%n2,"/",n2)