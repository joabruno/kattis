b = input().replace("-", "")
b_list = []
a = [4,3,2,7,6,5,4,3,2,1]
for i, i_n in enumerate(b):
    b_list.append(int(i_n)*a[i])



print(1 if sum(b_list)%11 == 0 else 0)