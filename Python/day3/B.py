def getValue(c: str) -> int:
    m = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return m.index(c) + 1


totalValue = 0
lines = open("./day3/input", "r").readlines()

for l in range(0, len(lines), 3):
    group = [lines[i].strip() for i in range(l, l+3)]

    for c in group[0]:
        if c in group[1] and c in group[2]:
            totalValue += getValue(c)
            break

print(totalValue)