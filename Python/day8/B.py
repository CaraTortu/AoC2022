import math

def GetDistance(trees, currTree):
    treeDistance = 0

    max = len(trees)-1

    for treeIndex, tree in enumerate(trees):
        if tree >= currTree or treeIndex == max:
            treeDistance += treeIndex+1
            break
    
    return treeDistance

def findScenicScore(row, col, map):
    treeDistance = {"l": 0, "r": 0, "t": 0, "b": 0}
    currentTree = map[row][col]

    # Get trees
    leftTrees   = map[row][0:col][::-1]
    rightTrees  = map[row][col+1:]
    topTrees    = [i[col] for i in map[0:rowIndex]][::-1]
    bottomTrees = [i[col] for i in map[rowIndex+1:]]

    # Calculate the distance to the left
    treeDistance["l"] = GetDistance(leftTrees, currentTree)
    
    # Calculate the distance to the right
    treeDistance["r"] = GetDistance(rightTrees, currentTree)

    # Calculate the distance to the top
    treeDistance["t"] = GetDistance(topTrees, currentTree)
    
    # Calculate the distance to the bottom
    treeDistance["b"] = GetDistance(bottomTrees, currentTree)
        
    return math.prod(treeDistance.values())


allTrees = [] 

for line in open("./day8/input").readlines():
    allTrees.append([int(i) for i in line.strip()])


maxScore = 0

for rowIndex, row in enumerate(allTrees):
    for columnIndex, column in enumerate(row):
        scenicScore = findScenicScore(rowIndex, columnIndex, allTrees)
        if scenicScore > maxScore:
            maxScore = scenicScore

print(maxScore)
