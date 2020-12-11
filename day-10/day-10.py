### ***** Advent of Code 2020 - Day 10 ***** ###

f = open("day-10-input.txt", "r")
input = f.readlines()
input = list(map(int, input))

input.sort()
input.insert(0, 0)
max = input[len(input)-1] + 3
input.append(max)

# Part 1
num1 = 0
num2 = 0
for i in range(1, len(input)):
    a1 = input[i-1]
    a2 = input[i]

    if a2 - a1 == 1:
        num1 += 1
    elif a2 - a1 == 3:
        num2 += 1

print(num1 * num2)

# Part 2 - using memoization
numAdapters = dict()
def getAdapters(numAdapters, adapters, max):
    if max == 0:
        return 1

    if numAdapters.get(max):
        return numAdapters.get(max)

    num = 0
    for a in adapters:
        if max - a >= 1 and max - a <= 3:
            num += getAdapters(numAdapters, adapters, a)
        elif max - a < 1:
            break

    numAdapters[max] = num
    return num

print(getAdapters(numAdapters, input, max))

# Part 2 - using DP
numAdapters = dict()
def getAdapters(numAdapters, adapters, max):
    if max == 0:
        return 1

    num = 0
    for i in range(1, 4):
        num += numAdapters.get(max-i, 0)
    return num

for a in input:
    numAdapters[a] = getAdapters(numAdapters, input, a)

print(getAdapters(numAdapters, input, max))
