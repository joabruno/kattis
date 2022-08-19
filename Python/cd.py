from sys import stdin
while True:
    jack, jill = [int(i) for i in input().split()]
    if (jack, jill) == (0,0):
        break
    large_set = set()
    largest, smallest = (jack, jill) if jack > jill else (jill, jack)
    largest_cd = 0
    for _ in range(smallest):
        inp = int(stdin.readline())
        large_set.add(inp)
        largest_cd = inp
    counter = 0
    for _ in range(largest):
        inp = int(stdin.readline())
        if inp > largest_cd:
            continue
        elif inp in large_set:
            counter += 1

    print(counter)