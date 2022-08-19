people, entries = input().split()

wallets = {}
reset = 0
for i in range(int(entries)):
    entry = input().split()
    if entry[0] == "SET":
        wallets[entry[1]] = int(entry[2])
    elif entry[0] == "PRINT":
        #print("test ", entry[1] in wallets)
        if entry[1] in wallets:
            print(wallets[entry[1]])
        else:
            print(reset)
    else:
        wallets = {}
        reset = entry[1]
    