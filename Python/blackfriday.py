participants = int(input())

part_list = []
outcomes = {}
outcomes_set = set()
for o in input().split():
    o = int(o)
    part_list.append(o)
    if o in outcomes_set:
        outcomes[o] += 1
    else:
        outcomes[o] = 1
        outcomes_set.add(o)
largest_unique = 0
for key, value in outcomes.items():
    if value == 1 and key > largest_unique:
        largest_unique = key
print(part_list.index(largest_unique)+1) if largest_unique != 0 else print("none")