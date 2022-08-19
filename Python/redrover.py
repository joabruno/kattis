x = input()
bestval = len(x)

for i in range(len(x)//2):
    substring = ""
    
    for c in x[i:(len(x)//2)+i]:
        substring += c
        print(substring)
        if len(substring) > 1:
            temp = x.replace(substring, "M")
            if len(temp) + len(substring) < bestval:
                bestval = len(temp) + len(substring)
print(bestval)