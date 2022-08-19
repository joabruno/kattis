a = input()
b = input().split()

sum = 10
tape_used = 0
papers_used = [0]* (int(a))
for index, paper in enumerate(b):
    pap = int(paper)
    if pap > 0:
        if 10*2**(-(index+1)) * pap> sum:
            papers_used[index+1] += sum/(10*2**(-(index+1)))
            sum = 0
            break
        else:
            sum -= 10*2**(-(index+1))*pap
            papers_used[index+1] += pap
#print(papers_used)
countie = 0
boolval = False
for ind, d in enumerate(reversed(papers_used)):
    if not boolval:
        if d <= 0:
            countie += 1
        else:
            boolval = True
    if d>=2 and int(a)-1 != 0:
        temp = d//2
        papers_used[-(ind+2)] += temp
        papers_used[-(ind+1)] = temp
        #print(ind % 2 == 0)
        tape_used += temp*(2**(-(3+(4*((int(a)-(ind+1))//2)))/4) if (ind - int(a)) % 2 == 0 else 2**(-(5+(4*(((int(a)-ind-2))//2)))/4))
if sum > 0:
    print("impossible")
else:
    print(tape_used)