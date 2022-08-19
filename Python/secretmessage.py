msgs = int(input())

for _ in range(msgs):
    inp = input()
    n = int(len(inp)**0.5) +1 if int(len(inp)**0.5) < len(inp)**0.5 else int(len(inp)**0.5)
    matrix = [["*" for _ in range(n)]for _ in range(n)]
    for i, c in enumerate(inp):
        row = (n-1) - (i//n)
        col = i % n
        #print(row)
        matrix[col][row] = c

    print("".join(["".join(x) for x in matrix]).replace("*", ""))