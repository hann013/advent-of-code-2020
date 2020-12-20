### ***** Advent of Code 2020 - Day 18 Part 1 ***** ###

f = open("day-18-input.txt", "r")
input = f.readlines()
# remove whitespace from each line
input = list(map(lambda i: i.strip().replace(" ", ""), input))

def getTotal(line, i):
    total, op = None, None
    while i < len(line):
        c = line[i]
        n = None

        if c == "+" or c == "*":
            # set next operation
            op = c
        elif c == "(":
            # set operand to the total between parentheses and set index to after closed parentheses
            n,i = getTotal(line, i+1)
        elif c == ")":
            break
        else:
            # set operand
            n = int(c)

        # do the operation if we have the second operand
        if n != None:
            if total == None:
                total = n
            elif op == "+":
                total += n
            elif op == "*":
                total *= n
        i += 1
    return (total,i)

results = []
for line in input:
    result = getTotal(line, 0)[0]
    results.append(result)

print(sum(results))

f.close()
