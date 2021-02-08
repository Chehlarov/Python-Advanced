line = input()

chars = {}

for c in line:
    if c not in chars:
        chars[c] = line.count(c)

sorted_result = sorted(chars.items(), key=lambda x: x[0])
for el in sorted_result:
    print(f"{el[0]}: {el[1]} time/s")
