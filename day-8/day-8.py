### ***** Advent of Code 2020 - Day 8 ***** ###
import copy

f = open("day-8-input.txt", "r")
input = f.readlines()

# Part 1
i = 0
acc = 0
executedLines = []

while True:
    op = input[i]
    code, num = op.split(" ")
    num = int(num)

    if code == "nop":
        # Go to next line
        i += 1
    elif code == "acc":
        # Add to accumulator and go to next line
        acc += num
        i += 1
    elif code == "jmp":
        # Jump to line
        i += num

    if i in executedLines:
        # Found duplicate instruction, terminate
        break
    else:
        executedLines.append(i)

print(acc)

# Part 2
def getResult(input):
    i = 0
    acc = 0
    executedLines = []

    while i < len(input):
        op = input[i]
        code, num = op.split(" ")
        num = int(num)

        if code == "nop":
            i += 1
        elif code == "acc":
            acc += num
            i += 1
        elif code == "jmp":
            i += num

        if i in executedLines:
            break
        else:
            executedLines.append(i)

    # Check if program terminated at last instruction (instead of loop)
    if i == len(input):
        print(acc)

# Try swapping inputs for each nop/jmp instruction
for i, line in enumerate(input):
    code, num = line.split(" ")
    newInput = copy.copy(input)

    if code == "nop":
        newInput[i] = "jmp " + num
        getResult(newInput)
    elif code == "jmp":
        newInput[i] = "nop " + num
        getResult(newInput)
