while True:
    inp = input()
    if inp == "0 0":
        break
    x,y = [int(o) for o in inp.split()]
    if x + y == 13:
        print("Never speak again.")
    elif x > y:
        print("To the convention.")
    elif x == y:
        print("Undecided.")
    else:
        print("Left beehind.")