photos = int(input())

hour = 0
miles = 0
max_speed = 0
input()
for _ in range(photos-1):
    h,m = input().split()
    if max_speed < (int(m)-miles)//(int(h)-hour):
        max_speed = (int(m)-miles)//(int(h)-hour)
    miles = int(m)
    hour = int(h)
print(max_speed)