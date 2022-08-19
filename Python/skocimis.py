x,y,z = input().split()

x,y,z = int(x), int(y), int(z)

m = max(y-x, z-y)

print(m-1)