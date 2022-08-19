for _ in range(int(input())):
    phone_numbers = [set() for _ in range(10)]
    phone_numbers_prefixes = [set() for _ in range(10)]
    consistent = True
    x = int(input())
    #print("here", x)
    for ix, _ in enumerate(range(x)):
        inp = input()
        inp_len = len(inp)
        #print("1", phone_numbers_prefixes[inp_len-1])
        #print("1", inp)
        if not consistent:
            #print("here1")
            for o in range(ix+1, x):
                input()
            break

        if inp in phone_numbers_prefixes[inp_len-1]:
            consistent = False
            #print("here2")
            for o in range(ix+1, x):
                input()
            break
        for i in range(inp_len):
                #print("2", inp[:i])
                #print("2", phone_numbers[(i)])
                if inp[:i+1] in phone_numbers[i]:
                    consistent = False
                    #print("here3")
                    #for o in range(ix+1, x):
                        #input()
                    break
                phone_numbers_prefixes[i].add(inp[:i+1])
        phone_numbers[inp_len-1].add(inp)
        #phone_numbers_list.append(inp)
    #print(phone_numbers)
    #print(phone_numbers_prefixes)      
    print("YES" if consistent else "NO")