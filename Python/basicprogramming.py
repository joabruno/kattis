n_nums, action = [int(i) for i in input().split()]
alph = "abcdefghijklmnopqrstuvwxyz"
if action == 1:
    input()
    print(7)
elif action == 2:
    nums = [int(i) for i in input().split()[:2]]
    print("Bigger" if nums[0] > nums[1] else ("Equal" if nums[0] == nums[1] else "Smaller"))
elif action == 3:
    nums = [int(i) for i in input().split()[:3]]
    print(sorted(nums)[1])
elif action == 4:
    print(sum([int(i) for i in input().split()]))
elif action == 5:
    print(sum([int(i) for i in input().split() if int(i) % 2 == 0]))
elif action == 6:
    print("".join([alph[int(i)%26] for i in input().split()]))
elif action == 7:
    nums = [int(i) for i in input().split()]
    nums_set = set()
    index = 0
    while index < len(nums)-1:
        if nums[index] not in nums_set:
            nums_set.add(nums[index])
            index = nums[index]
        else:
            print("Cyclic")
            break
    if index >= len(nums)-1:
        print("Out" if index > (len(nums)-1) else "Done")