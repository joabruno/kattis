var_env = {}
var_set = set()
val_set = set()
while True:
    try:
        inp = input().split()
    except:
        break
    if inp[0] == "def":
        var_env[inp[1]] = int(inp[2])
        var_set.add(inp[1])
    elif inp[0] == "calc":
        output = ""
        for i, val in enumerate(inp[1:]):
            if val == "=":
                eval_val = eval(output)
                var_name = ""
                for key, value in var_env.items():
                    if value == eval_val:
                        var_name = key
                if var_name == "":
                    print(" ".join(inp[1:]) + " unknown")
                else:
                    print(" ".join(inp[1:]) + " " + var_name)
            elif i % 2 == 0:
                if val not in var_set:
                    print(" ".join(inp[1:]) + " unknown")
                    break
                else:
                    output += str(var_env[val]) + " "
            else:
                output += val + " "
    else:
        var_env = {}
        var_set = set()
        val_set = set()

500
250
125
67
33
16
8
4
2
1