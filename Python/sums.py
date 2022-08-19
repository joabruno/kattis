counter = 1
while True:
    try:
        num = int(input())
        print("Case {0}:".format(counter))
        counter +=1
    except EOFError:
        break

    numbers = []
    sums = []
    for _ in range(num):
        inp = int(input())
        sums += [x + inp for x in numbers]
        #print(sums)
        numbers.append(inp)
        #print(numbers)
    num_of_queries = int(input())
    for _ in range(num_of_queries):
        closest = 100000000
        query = int(input())
        for n in sums:
            if abs(n-query) < closest:
                closest = abs(n-query)
                out = n
        print("Closest sum to {0} is {1}.".format(query, out))