### ***** Advent of Code 2020 - Day 12 Part 2 ***** ###

f = open("day-12-input.txt", "r")
input = f.readlines()

def getVal(direction):
    return int(direction[1:])

def turn(degrees):
    degrees = degrees // 90
    for i in range(abs(degrees)):
        # Rotate 90 degrees
        temp = waypoint[0]
        waypoint[0] = waypoint[1]
        waypoint[1] = temp

        if degrees < 0:
            waypoint[1] = -waypoint[1]
        else:
            waypoint[0] = -waypoint[0]

ship = [0, 0]
waypoint = [1, 10]

for d in input:
    action = d[0]
    val = getVal(d)

    if action == "N":
        waypoint[0] += val
    elif action == "S":
        waypoint[0] -= val
    elif action == "E":
        waypoint[1] += val
    elif action == "W":
        waypoint[1] -= val
    elif action == "L":
        turn(-val)
    elif action == "R":
        turn(val)
    elif action == "F":
        ship[0] += waypoint[0] * val
        ship[1] += waypoint[1] * val

print(abs(ship[0]) + abs(ship[1]))

f.close()
