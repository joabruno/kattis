for _ in range(int(input())):
    x,y = input().split()
    
    posints = sum([i for i in range(1,(int(y)+1))])
    oddints = sum([i for i in range(1,(int(y)*2), 2)])
    evenints = sum([i for i in range(0,((int(y)+1)*2), 2)])

    
    print("{0} {1} {2} {3}".format(x,posints,oddints,evenints))