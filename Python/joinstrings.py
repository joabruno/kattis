from sys import stdin, stdout


n = int(stdin.readline())

class streng():
  smallest_child = None
  next_str = None
  largest_parent = None
  v = None


string_dic = []
if n == 1:
  print(input())
else:
  for i in range(n):
    ss = streng()
    ss.smallest_child = ss
    ss.largest_parent = ss
    ss.v = stdin.readline().replace("\n", "")
    string_dic.append(ss)
  l = ""
  for _ in range(n-1):
    a,b = [int(d)-1 for d in stdin.readline().split()]
    string_dic[a].smallest_child.next_str = string_dic[b]
    string_dic[a].smallest_child = string_dic[b].smallest_child
    string_dic[b].gf = string_dic[a].gf
    l = a

  string_dic[a].gf.smallest_child.smallest_child = None
  x = string_dic[a].gf
  while x != None:
    stdout.write(x.v)
    x = x.next_str

