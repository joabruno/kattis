people, chicken = [int(x) for x in input().split()]

if chicken >= people:
    if chicken-people == 1:
        print("Dr. Chaz will have {} piece of chicken left over!".format(chicken-people))
    else:
        print("Dr. Chaz will have {} pieces of chicken left over!".format(chicken-people))
else:
    if people-chicken == 1:
        print("Dr. Chaz needs {} more piece of chicken!".format(people-chicken))
    else:
        print("Dr. Chaz needs {} more pieces of chicken!".format(people-chicken))
    
