f = open("./day1/input", "r").readlines()

elfs = []
i = 0

for line in f:
    if line == "\n":
        i+=1
        continue

    if i-1 < len(elfs):
        elfs.append(0)

    elfs[i] += int(line)

print(max(elfs))