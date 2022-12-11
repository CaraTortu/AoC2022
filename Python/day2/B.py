inp = open("./day2/input", "r").readlines()

ch = {
    "A": {
        "X": 3,
        "Y": 4,
        "Z": 8
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 2,
        "Y": 6,
        "Z": 7
    }
}

score = 0

for line in inp:
    elf, me = line.strip().split(" ")
    score += ch[elf][me]

print(score)