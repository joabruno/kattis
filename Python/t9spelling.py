cases = int(input())

enc_dict = {
    "abc": "2",
    "def": "3",
    "ghi": "4",
    "jkl": "5",
    "mno": "6",
    "pqrs": "7",
    "tuv": "8",
    "wxyz": "9",
    " ": "0"}

for i in range(1,cases+1):
    prev = None
    inp = input()
    out= ""
    for c in inp:
        for key, value in enc_dict.items():
            if c in key:
                out += value * (key.index(c)+1) if key != prev else " " +value * (key.index(c)+1)
                prev = key
    print("Case #%d: %s" % (i, out))