### ***** Advent of Code 2020 - Day 15 ***** ###

input = [0,13,1,8,6,15]

def getNumber(numTurns):
    turn = 1
    numSpoken = 0
    # Keep track of up to the two latest turns that the number was spoken
    spokenTimes = dict()

    while turn <= numTurns:
        if turn-1 < len(input):
            # Read the starting numbers
            numSpoken = input[turn-1]
            spokenTimes[numSpoken] = [turn]
        else:
            if len(spokenTimes[numSpoken]) < 2:
                # The number has only been read once
                numSpoken = 0
            else:
                # The number has been read more than once
                times = spokenTimes[numSpoken]
                numSpoken = times[1] - times[0]
                times.pop(0)

            # Store the turn number for the new numSpoken
            if spokenTimes.get(numSpoken):
                spokenTimes[numSpoken].append(turn)
            else:
                spokenTimes[numSpoken] = [turn]
        turn += 1

    return numSpoken

# Part 1
print(getNumber(2020))

# Part 2
print(getNumber(30000000))
