string = (input())
symbol_count = {}
forward = len(string)
for i in range(len(string)):
    if string[i] not in symbol_count.keys():
        symbol_count[string[i]] = (forward - i) * (i + 1)
    else:
        symbol_count[string[i]] += (forward - i) * (i + 1)
    
for (k, v) in sorted(symbol_count.items()):
    print("{}: {}".format(k, v))
