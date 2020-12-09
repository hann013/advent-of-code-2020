### ***** Advent of Code 2020 - Day 2 ***** ###

# Part 1
def isValidOne(limits, letter, password):
    minLetters, maxLetters = limits
    numLetters = 0

    for l in password:
        if l == letter:
            numLetters += 1

    return numLetters >= minLetters and numLetters <= maxLetters

# Part 2
def isValidTwo(positions, letter, password):
    pos1, pos2 = positions

    # Convert positions to zero-indices
    letterAt1 = password[pos1 - 1] == letter
    letterAt2 = password[pos2 - 1] == letter

    return (letterAt1 or letterAt2) and not (letterAt1 and letterAt2)

f = open("day-2-input.txt", "r")
input = f.read().splitlines()
numValidOne = 0
numValidTwo = 0

for line in input:
    # Parse input into limits, target letter, and the password string
    policy, password = line.split(": ")

    limits, letter = policy.split(" ")
    limits = list(map(lambda n: int(n), limits.split("-")))

    if isValidOne(limits, letter, password):
        numValidOne += 1
    if isValidTwo(limits, letter, password):
        numValidTwo += 1

print(numValidOne, numValidTwo)

f.close()
