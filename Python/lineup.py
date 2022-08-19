x = int(input())

members = []
for _ in range(x):
    members.append(input())

sorted_members = sorted(members)
sorted_reverse_members = sorted(members)
sorted_reverse_members.reverse()

if members == sorted_members:
    print("INCREASING")
elif members == sorted_reverse_members:
    print("DECREASING")
else:
    print("NEITHER")