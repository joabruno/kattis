guess = 500
gu = 500
g = 1
while True:
    print(guess, flush=True)
    if gu/(2**g) < gu//(2**g) + 0.5:
        guesses = gu//(2**g)
    else:
        guesses = gu//(2**g)+1
    try:
        inp = input()
    except:
        break
    if inp == "lower":

        guess -= guesses
    elif inp == "higher":
        guess += guesses
    else:
        break