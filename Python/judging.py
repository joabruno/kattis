submissions = int(input())

submission_dict = {}
submission_dict2 = {}

l1 = []
counter = 0
for _ in range(submissions):
    inp = input()
    if counter < submissions:
        if inp not in submission_dict:
            submission_dict[inp] = 1
        else:
            submission_dict[inp] += 1
    else:
        if inp not in submission_dict2:
            submission_dict2[inp] = 1
        else:
            submission_dict2[inp] += 1
    counter += 1
    inp = input()
    if counter < submissions:
        if inp not in submission_dict:
            submission_dict[inp] = 1
        else:
            submission_dict[inp] += 1
    else:
        if inp not in submission_dict2:
            submission_dict2[inp] = 1
        else:
            submission_dict2[inp] += 1
    counter += 1
sum = 0
for x in submission_dict:
    if x in submission_dict2:
        sum += min(submission_dict[x],submission_dict2[x])
print(sum)