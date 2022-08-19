sounds = {
    "clank": "A",
    "bong": "B",
    "click": "C",
    "tap": "D",
    "poing": "E",
    "clonk": "F",
    "clack": "G",
    "ping": "H",
    "tip": "I",
    "cloing": "J",
    "tic": "K",
    "cling": "L",
    "bing": "M",
    "pong": "N",
    "clang": "O",
    "pang": "P",
    "clong": "Q",
    "tac": "R",
    "boing": "S",
    "boink": "T",
    "cloink": "U",
    "rattle": "V",
    "clock": "W",
    "toc": "X",
    "clink": "Y",
    "tuc": "Z",
    "whack": " "
}

letters = int(input())
lower = True
out = ""
for _ in range(letters):
    inp = input()
    if inp == "bump":
        lower = not lower
    elif inp == "pop":
        out = out[:-1]
    elif inp == "dink" or inp == "thumb":
        lower = not lower
    else:
        out += sounds[inp] if not lower else sounds[inp].lower()
print(out)