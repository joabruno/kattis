n1,n2,n3 = input().split()

nums = sorted([int(n1), int(n2), int(n3)])


output= ""
for c in input():
    if c =="A":
        output += str(nums[0]) + " "
    elif c =="B":
        output += str(nums[1]) + " "
    else:
        output += str(nums[2]) + " "

print(output[:-1])