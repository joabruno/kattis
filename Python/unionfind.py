from sys import stdin
base, queries = [int(i) for i in stdin.readline().split()] 
sets_dic = {}
char_to_key = {}
sets_in_dic = set()
for _ in range(queries):
    operation, first, second = stdin.readline().split()
    if operation == "?":
        if first == second:
            print("yes")
        elif first not in sets_in_dic or second not in sets_in_dic:
            print("no")
        else:
            print("no" if sets_dic[char_to_key[first]] != sets_dic[char_to_key[first]] else "yes")
    else:
        if first in sets_in_dic and second in sets_in_dic:
            set_1 = set(first)
            set_2 = set(second)
            key_1 = first
            key_2 = second

            if char_to_key[key_1] != char_to_key[key_2]:
                set_1 = sets_dic.pop(key_1, None)
                set_2 = sets_dic.pop(key_2, None)
                char_to_key[key_1] = char_to_key[key_1]+char_to_key[key_2]
                char_to_key[key_2] = char_to_key[key_1]+char_to_key[key_2]
                for c in char_to_key[key_1]:
                    char_to_key[c] = char_to_key[key_1]
                sets_dic[char_to_key[key_1]+char_to_key[key_2]] = set_1.union(set_2)
            else:
                continue
        elif first in sets_in_dic or second in sets_in_dic:
            set_1 = set(first)
            set_2 = set(second)
            key_1 = first
            key_2 = second
            if key_1 in sets_in_dic:
                set_1 = sets_dic.pop(char_to_key[key_1], None)
                char_to_key[key_1] = char_to_key[key_1]+(key_2,)
                char_to_key[key_2] = char_to_key[key_1]+(key_2,)
                sets_in_dic.add(second)
                for c in char_to_key[key_1]:
                    char_to_key[c] = char_to_key[key_1]
                sets_dic[char_to_key[key_1]] = set_2.union(set_1)
            else:
                set_2 = sets_dic.pop(char_to_key[key_2], None)
                char_to_key[key_1] = (key_1,)+char_to_key[key_2]
                char_to_key[key_2] = (key_1,)+char_to_key[key_2]
                sets_in_dic.add(first)
                for c in char_to_key[key_2]:
                    char_to_key[c] = char_to_key[key_2]
                sets_dic[char_to_key[key_2]] = set_1.union(set_2)
        else:
            sets_in_dic.add(first)
            sets_in_dic.add(second)
            set_1 = set(first)
            set_2 = set(second)
            key_1 = first
            key_2 = second
            char_to_key[key_1] = (key_1, key_2)
            char_to_key[key_2] = (key_1, key_2)
            sets_dic[(key_1, key_2)] = set_1.union(set_2)