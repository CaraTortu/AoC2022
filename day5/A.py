import math
import re

def getCrates(f: str) -> list:
    crates = [[] for i in range(math.floor(len(f[0])/4))]

    for l in f:
        l = l.replace("\n", "")

        for i in range(0, len(l), 4):
            toAppend = l[i:i+4].strip().replace("[", "").replace("]", "")
            if toAppend != "":
                crates[int(i/4)].append(toAppend)
    
    return crates

fullInput = open("./day5/input").readlines()

i = fullInput.index("\n")
cs, cmds = (fullInput[0:i], fullInput[i:])

cs.pop(-1)


crates = getCrates(cs)

ccs = []

for i in cmds:
    toAppend = [int(k) for k in re.sub("\D", "", i.strip())]
    if toAppend != []:
        if len(toAppend) == 4:
            toAppend[0] = int(str(toAppend[0])+ str(toAppend[1]))
            del toAppend[1]
        ccs.append(toAppend)

for cmd in ccs:

    for crate in crates[cmd[1]-1][0:cmd[0]]:
        crates[cmd[2]-1].insert(0, crate)
    
    for i in range(0, cmd[0]):
        crates[cmd[1]-1].pop(0)

print(''.join([i[0] for i in crates]))