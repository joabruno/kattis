inp = input()

output = []

for c in inp:
    if c == "<":
        output.pop()
    else:
        output.append(c)
print("".join(output))