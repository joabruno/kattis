first = True
while True:

    n_names = int(input())
    if n_names == 0:
        break
    if not first:
        print()
    
    names = []

    for _ in range(n_names):
        names.append(input())

    first2 = [s[:2] for s in names]
    newlist = []
    for i,n in enumerate(first2):
        print(names[sorted(first2).index(n)])
    first = False