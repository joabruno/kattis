vol = 7

for _ in range(int(input())):
    x = input()
    if x == "Skru op!" and vol != 10:
        vol += 1
    elif x == "Skru ned!" and vol != 0:
        vol -= 1
    
print(vol)