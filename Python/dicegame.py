g = sum([int(i) for i in input().split()])
e = sum([int(i) for i in input().split()])

if g > e:
    print("Gunnar")
elif e > g:
    print("Emma")
else:
    print("Tie")