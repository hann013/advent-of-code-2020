### ***** Advent of Code 2020 - Day 3 ***** ###

f = open("day-3-input.txt", "r")
input = f.read().splitlines()
numLines = len(input)
lineLength = len(input[0])

tree = "#"

# Part 1
numTrees = 0
index = 0

for line in input:
    if line[index] == tree:
        numTrees += 1

    # Calculate and store next index
    index = (index + 3) % lineLength

print(numTrees)

# Part 2

# each inner array denotes number of steps to the right, current index, and number of trees
numTrees = [[1, 0, 0], [3, 0, 0], [5, 0, 0], [7, 0, 0]]
numTreesEveryOtherRow = 0
everyOtherRowIndex = 0

for i, line in enumerate(input):
    for data in numTrees:
        steps, index, num = data
        if line[index] == tree:
            data[2] = num + 1

        # Calculate and store next index
        data[1] = (index + steps) % lineLength

    # Every other line
    if i % 2 == 0:
        if line[everyOtherRowIndex] == tree:
            numTreesEveryOtherRow += 1

        # Calculate and store next index
        everyOtherRowIndex = (everyOtherRowIndex + 1) % lineLength

product = numTreesEveryOtherRow
for data in numTrees:
    product *= data[2]
print(product)
