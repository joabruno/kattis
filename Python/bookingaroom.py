rooms, booked = [int(i) for i in input().split()]

booked_list = []

for _ in range(booked):
    booked_list.append(int(input()))

if len(booked_list) >= rooms:
    print("too late")
else:
    for i in range(1, rooms+1):
        if i not in booked_list:
            print(i)
            break