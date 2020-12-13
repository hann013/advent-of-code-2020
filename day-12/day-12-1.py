### ***** Advent of Code 2020 - Day 12 Part 1 ***** ###

f = open("day-12-input.txt", "r")
input = f.readlines()

def getVal(direction):
    return int(direction[1:])

# north = [0, 1]
# east = [1, 1]
# south = [0, -1]
# west = [1, -1]
def turn(degrees):
    degrees = degrees // 90
    for i in range(abs(degrees)):
        target = 0 if degrees < 0 else 1
        nextBearing = 1 if degrees < 0 else 0

        # Rotate 90 degrees
        if bearing[0] == target:
            bearing[0] = nextBearing
            bearing[1] = -bearing[1]
        else:
            bearing[0] = target

ship = [0, 0]
bearing = [1, 1]

for d in input:
    action = d[0]
    val = getVal(d)

    if action == "N":
        ship[0] += val
    elif action == "S":
        ship[0] -= val
    elif action == "E":
        ship[1] += val
    elif action == "W":
        ship[1] -= val
    elif action == "L":
        turn(-val)
    elif action == "R":
        turn(val)
    elif action == "F":
        ship[bearing[0]] += bearing[1] * val

print(abs(ship[0]) + abs(ship[1]))

f.close()
