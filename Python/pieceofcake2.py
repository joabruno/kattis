x,y,z = [int(i) for i in input().split()]

print(max(x-y,y)*max(x-z,z)*4)
