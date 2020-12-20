### ***** Advent of Code 2020 - Day 19 Part 1 ***** ###

# for each rule, either:
# parse it into its rule number and the matching character
# parse it into its rule number and an array of rules
# parse it into its rule number and arrays of rules (for or conditions)
def parseRule(rule):
    parts = rule.strip().split(": ")
    index = int(parts[0])
    contents = parts[1]

    if "\"" in contents:
        contents = contents[1]
    elif "|" in contents:
        contents = contents.split(" | ")
        contents = list(map(lambda c: list(map(int, c.split(" "))), contents))
    else:
        contents = list(map(int, contents.split(" ")))
    return (index, contents)

# recursively check whether a given rule matches
# return whether or not it matches, and the next char index of the message to check
def matchesRule(rules, ri, msg, mi):
    rule = rules.get(ri)

    if type(rule) is str:
        # check whether or not the message's char matches the rule's char
        return (msg[mi] == rule, mi+1)
    elif type(rule[0]) is int:
        # check whether or not each rule in the array is satisfied
        match = True
        for n in rule:
            m, ni = matchesRule(rules, n, msg, mi)
            match = match and m
            if match == False:
                break
            mi = ni
        return (match, mi)
    else:
        # for each rule array, check whether or not it's satisfied
        # the rule is satisfied if any array is satisfied
        match = False
        oldmi = mi
        for group in rule:
            matchGroup = True
            for n in group:
                m, ni = matchesRule(rules, n, msg, mi)
                matchGroup = matchGroup and m
                if matchGroup == False:
                    break
                mi = ni
            match = match or matchGroup
            if match == True:
                break
            # reset the message char index before checking new rule array
            mi = oldmi
        return (match, mi)

f = open("day-19-input-1.txt", "r")
input = f.readlines()

i = input.index("\n")
rules = input[:i]
parsedRules = dict()
for rule in rules:
    index, contents = parseRule(rule)
    parsedRules[index] = contents

messages = input[i+1:]
count = 0

for msg in messages:
    match, mi = matchesRule(parsedRules, 0, msg, 0)
    if match and mi == len(msg)-1:
        count += 1

print(count)

f.close()
