while True:
    try:
        numbers = input().split()
    except EOFError:
        break

    print(abs(int(numbers[0])- int(numbers[1])))