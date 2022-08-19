
from re import I


table = []
for _ in range(int(input())):
    table.append([int(x) for x in input().split()])


for index, i in enumerate(table[0]):
    if i == 0:
        continue
    else:
        for j in table[index]:
            if j == 0:
                continue
            else:
                if i < j:
                    break
                print("%d %d" % (1, index+1))
