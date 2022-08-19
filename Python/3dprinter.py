statues = int(input())

printers = 1
days_passed = 0

while printers < statues:
    printers = printers *2
    days_passed += 1

print(days_passed+1)