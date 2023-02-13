import re
from sys import stdin

symbols = stdin.read()
symbols = re.sub(r"\s+", "", symbols, flags=re.UNICODE)
count_symbols = {symbol: symbols.count(symbol) for symbol in symbols}
sorted_keys = sorted(count_symbols.keys())
for i in range(max(count_symbols.values()), 0, -1):
    for symbol in sorted_keys:
        if count_symbols.get(symbol) >= i:
            print("#", end="")
        else:
            print(" ", end="")
    print()
print("".join(sorted_keys))
