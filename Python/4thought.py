four = str(4)
symbols = ["*","+","-","//"]
numb = {}
for s_1 in symbols:
    for s_2 in symbols:
        for s_3 in symbols:
            equ = four + " "  +s_1 + " " +four + " " +s_2 +" " + four +" " + s_3 +" " + four
            res = int(eval(equ))
            numb[res] = equ.replace("//", "/") + " = " + str(res)
for _ in range(int(input())):
    k= int(input())
    print(numb[k] if k in numb else "no solution")