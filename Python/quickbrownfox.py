alphabet = "abcdefghijklmnopqrstuvwxyz"

cases = int(input())

for c in range(cases):
    inp = input().lower()
    out = ""
    for a in alphabet:
        if a not in inp:
            out += a
    print("pangram" if out == "" else "missing %s" % out)