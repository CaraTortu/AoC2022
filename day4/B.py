def overlapping(A: list, B: list) -> bool:
    for i in A:
        if i in B:
            return True
    return False

overlap = 0

for line in open("./day4/input").readlines():
    line = line.strip()
    
    elfA, elfB = line.split(",")

    elfAStart, elfAEnd = elfA.split("-")
    elfBStart, elfBEnd = elfB.split("-")

    elfARange = list(range(int(elfAStart), int(elfAEnd)+1))
    elfBRange = list(range(int(elfBStart), int(elfBEnd)+1))

    if overlapping(elfARange, elfBRange) or overlapping(elfBRange, elfARange):
        overlap += 1

print(overlap)