from sys import stdin
for _ in range(int(stdin.readline())):
    phone_numbers = [set() for _ in range(10)]
    phone_numbers_list = []
    consistent = True
    for _ in range(int(stdin.readline())):
        inp = stdin.readline().replace('\n', '')
        #print("2", inp)
        inp_len = len(inp)
        phone_numbers[inp_len-1].add(inp)
        phone_numbers_list.append(inp)
    for p_n in phone_numbers_list:
            pn_len = len(p_n)
            if not consistent:
                break
            for i in range(pn_len):
                #print(p_n[:i] in phone_numbers[(i-1)])
                if p_n[:i] in phone_numbers[(i-1)]:
                    consistent = False
                    break
    print("Yes" if consistent else "No")