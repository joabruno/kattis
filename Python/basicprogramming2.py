n_numbers, action = [int(i) for i in input().split()]

if action == 1:
    #time limit
    numbers = set()
    seven = False
    for num in input().split():
        num_i = int(num)
        numbers.add(num_i)
        if 7777-num_i in numbers:
            seven = True
            
    print("Yes" if seven else "No")
elif action == 2:
    #fejler case 12 og 13
    numbers = []
    numbers_set = set()
    for i in input().split():
        numbers.append(i)
        numbers_set.add(i)

    print("Unique" if sorted(numbers) == list(sorted(numbers_set)) else "Contains duplicate")
elif action == 3:
    numbers_dict = {}
    numbers_set = set()
    for x in input().split():
        if x in numbers_set:
            numbers_dict[x] += 1
        else:
            numbers_dict[x] = 1
            numbers_set.add(x)
    repeating = False
    repeating_number = "-1"
    for key, value in numbers_dict.items():
        if value > n_numbers/2:
            repeating = True
            repeating_number = key
    print(repeating_number)
elif action == 4:
    numbers = [int(i) for i in input().split()]
    numbers.sort()
    #print(numbers)
    print(numbers[n_numbers//2] if n_numbers % 2 == 1 else "%d %d" % (numbers[(n_numbers//2)-1], numbers[n_numbers//2]))
elif action == 5:
    numbers = [i for i in input().split() if int(i) in range(100,1000)]
    print(" ".join(sorted(numbers)))