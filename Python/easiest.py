while True:
    number = input()
    if number == "0":
        break
    

    num_sum = sum([int(x) for x in number])

    for i in range(11,101):
        new_sum = sum(int(x) for x in str(int(number)*i))
        if new_sum == num_sum:
            print(i)
            break