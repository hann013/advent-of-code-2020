### ***** Advent of Code 2020 - Day 18 Part 2 ***** ###

f = open("day-18-input.txt", "r")
input = f.readlines()
# remove whitespace
input = list(map(lambda i: i.strip().replace(" ", ""), input))

def insertLeftParentheses(line, i):
    findOpenBrackets = 0
    while i >= 0:
        c = line[i]

        # if we come across a closed parentheses, ignore everything until after the corresponding open parentheses
        if c == ")":
            findOpenBrackets += 1
        elif c == "(":
            # no more corresponding parentheses to consider, so found spot
            if findOpenBrackets == 0:
                break
            findOpenBrackets -= 1
        # no open parentheses to consider, so we want to add it right before a * operation
        elif c == "*" and findOpenBrackets == 0:
            break
        i -= 1
    line = line[:i+1] + "(" + line[i+1:]
    return line

def insertRightParentheses(line, i):
    findCloseBrackets = 0
    while i < len(line):
        c = line[i]

        # if we come across an open parentheses, ignore everything until after the corresponding closed parentheses
        if c == "(":
            findCloseBrackets += 1
        elif c == ")":
            # no more corresponding parentheses to consider, so found spot
            if findCloseBrackets == 0:
                break
            findCloseBrackets -= 1
        # no closed parentheses to consider, so we want to add it right before a * operation
        elif c == "*" and findCloseBrackets == 0:
            break
        i += 1
    line = line[:i] + ")" + line[i:]
    return line

# add parentheses around numbers on both sides of + operator to indicate precedence
def addParentheses(line, i):
    while i < len(line):
        c = line[i]
        if c == "+":
            line = insertLeftParentheses(line, i)
            # i has increased due to addition of left parentheses
            line = insertRightParentheses(line, i+1)
            # i increases again due to addition of right parentheses
            i += 1
        i += 1
    return line

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
    line = addParentheses(line, 0)
    result = getTotal(line, 0)[0]
    results.append(result)

print(sum(results))

f.close()
