def getValue(c: str) -> int:
    m = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return m.index(c) + 1


totalValue = 0

for l in open("./day3/input", "r").readlines():
    l = l.strip()

    partLength = int(len(l)/2)
    firstPart = l[0:partLength]
    lastPart = l[partLength:]

    for c in firstPart:
        if c in lastPart:
            totalValue += getValue(c)
            break

print(totalValue)