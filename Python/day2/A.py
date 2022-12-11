inp = open("./day2/input", "r").readlines()

ch = {
    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6
    }
}

score = 0

for line in inp:
    elf, me = line.strip().split(" ")

    score += ch[elf][me]

print(score)