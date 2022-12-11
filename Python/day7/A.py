
def parseCommand(l: list, files, path) -> None:
    files = files["/"]

    for p in path:
        files = files[p]

    command = l[0].replace("$ ", "")

    if command.startswith("ls"):
        for file in l[1:]:
            size, name = file.split(" ")

            if size.isdigit():
                files[name] = size
            else:
                files[name] = {}

    if command.startswith("cd"):
        command, p = command.split(" ")
        if p == "..":
            path.pop(-1)
        else:
            path.append(p)
    
def getFolderSize(folder: dict, path: list) -> int:
    global size

    tmp = folder[path[0]]
    total = 0

    for p in path[1:]:
        tmp = tmp[p]

    for file in tmp:
        if type(tmp[file]) is dict:
            total += getFolderSize(folder, path + [file])
        else:
            total += int(tmp[file])

    if total <= 100000:
        size += total

    return total

files = {"/": {}}
path = []
commands = [[]]

## GET ALL COMMANDS

i = -1

for l in open("./day7/input", "r").readlines():
    l = l.strip()

    if l.startswith("$ "):
        i += 1
        commands.append([])
    
    commands[i].append(l)

## Follow commands

commands = commands[1:-1] # clean

for command in commands:
    parseCommand(command, files, path)

## Get sizes
size = 0

getFolderSize(files, ["/"])

print(f"All sizes: {size}")