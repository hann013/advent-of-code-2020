### ***** Advent of Code 2020 - Day 19 Part 2 ***** ###

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
# return whether or not it matches, the next char index of the message to check,
# along with the number of times it matched the rule (only relevant for rules 8 and 11)
def matchesRule(rules, ri, msg, mi):
    rule = rules.get(ri)

    if ri == 0:
        m8, ni, count42 = matchesRule(rules, 8, msg, mi)
        mi = ni
        m11, ni, count31 = matchesRule(rules, 11, msg, mi)
        mi = ni

        # rule 0 is only satisfied if both rules 42 and 31 were satisfied at least once,
        # and the number of times rule 42 was satisfied > the number of times rule 31 was satisfied
        # (in order to guarantee rule 8 was satisfied)
        foundMatch = m8 and m11 and count42 > count31
        return (foundMatch, mi, 0)

    if ri == 8 or ri == 11:
        nextRule = 42 if ri == 8 else 31

        # try to find at least one match for the next rule
        m, ni, num = matchesRule(rules, nextRule, msg, mi)
        mi = ni

        if m == False:
            return (m, mi, 0)

        count = 1
        match = True
        # try to find as many more matches as possible
        while match == True:
            m, ni, num = matchesRule(rules, nextRule, msg, mi)
            if m == False:
                # break to return the last found match
                break
            mi = ni
            count += 1
        return (match, mi, count)

    else:
        if type(rule) is str:
            # check whether or not the message's char matches the rule's char
            return (msg[mi] == rule, mi+1, 0)
        elif type(rule[0]) is int:
            # check whether or not each rule in the array is satisfied
            match = True
            for n in rule:
                m, ni, count = matchesRule(rules, n, msg, mi)
                match = match and m
                if match == False:
                    break
                mi = ni
            return (match, mi, 0)
        else:
            # for each rule array, check whether or not it's satisfied
            # the rule is satisfied if any array is satisfied
            match = False
            oldmi = mi
            for group in rule:
                matchGroup = True
                for n in group:
                    m, ni, count = matchesRule(rules, n, msg, mi)
                    matchGroup = matchGroup and m
                    if matchGroup == False:
                        break
                    mi = ni
                match = match or matchGroup
                if match == True:
                    break
                # reset the message char index before checking new rule array
                mi = oldmi
            return (match, mi, 0)

f = open("day-19-input-2.txt", "r")
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
    match, mi, num = matchesRule(parsedRules, 0, msg, 0)
    if match and mi == len(msg)-1:
        count += 1

print(count)

f.close()
