### ***** Advent of Code 2020 - Day 5 ***** ###
def getID(bp):
    rows = [0, 127]
    row = 0

    # get row from first 7 letters
    for i in range(7):
        letter = bp[i]
        if letter == "F":
            if i == 6:
                row = rows[0]
            else:
                rows[1] = (rows[0] + rows[1]) // 2
        elif letter == "B":
            if i == 6:
                row = rows[1]
            else:
                rows[0] = (rows[0] + rows[1]) // 2 + 1

    cols = [0, 7]
    col = 0

    # get column from last 3 letters
    for i in range(7, 10):
        letter = bp[i]
        if letter == "L":
            if i == 9:
                col = cols[0]
            else:
                cols[1] = (cols[0] + cols[1]) // 2
        elif letter == "R":
            if i == 9:
                col = cols[1]
            else:
                cols[0] = (cols[0] + cols[1]) // 2 + 1

    return row * 8 + col

f = open("day-5-input.txt", "r")
input = f.read().splitlines()

# Part 1
highestID = 0
for bp in input:
    id = getID(bp)
    if id > highestID:
        highestID = id

print(highestID)

# Part 2
ids = list(map(getID, input))
ids.sort()

for i in range(1, len(ids)):
    id1 = ids[i-1]
    id2 = ids[i]
    if id2 - id1 > 1:
        print(id1+1)
