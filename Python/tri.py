x,y,z = [int(i) for i in input().split()]

operators = ["+", "-", "/", "*"]

for operator in operators:
    if eval("%d %s %d" % (x, operator, y)) == z:
        print("%d%s%d=%d" % (x, operator, y, z))
        break
    elif eval("%d %s %d" % (y, operator, z)) == x:
        print("%d=%d%s%d" % (x, y, operator, z))
        break