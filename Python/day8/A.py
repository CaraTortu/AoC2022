def clamp(num, min_value, max_value):
        return max(min(num, max_value), min_value)

allTrees = [] 

for line in open("./day8/input").readlines():
    allTrees.append([int(i) for i in line.strip()])

width = len(allTrees[0])-1
height = len(allTrees)-1

visibleTrees = 0

for rowIndex, row in enumerate(allTrees):
    for columnIndex, column in enumerate(row):
        if rowIndex == 0 or columnIndex == 0 or rowIndex == height or columnIndex == width:
            visibleTrees += 1
            continue

        elif column > max(row[0:columnIndex]) or column > max(row[columnIndex+1:]) or column > max([i[columnIndex] for i in allTrees[0:rowIndex]]) or column > max([i[columnIndex] for i in allTrees[rowIndex+1:]]):
            visibleTrees += 1

print(visibleTrees)
