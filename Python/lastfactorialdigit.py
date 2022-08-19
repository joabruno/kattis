cases = int(input())

for _ in range(cases):
    fac_sum = 1
    new_inp = int(input())
    while new_inp > 0:
        fac_sum *= new_inp
        new_inp -= 1
    print(str(fac_sum)[-1])