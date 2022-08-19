for _ in range(int(input())):
    phone_numbers = set()
    phone_numbers_list = []
    consistent = True
    for _ in range(int(input())):
        inp = input()
        phone_numbers.add(inp)
        phone_numbers_list.append(inp)
    for inp in phone_numbers_list:
        for i in range(len(inp)):
            if inp[:-i] in phone_numbers:
                consistent = False
                break
    print("Yes" if consistent else "No")