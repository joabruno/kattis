
distinct_nums = []
for _ in range(10):
    mod_42 = int(input()) % 42
    if mod_42 not in distinct_nums:
        distinct_nums.append(mod_42)

print(len(distinct_nums))