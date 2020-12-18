### ***** Advent of Code 2020 - Day 16 ***** ###

def parseRule(rule):
    name, vals = rule.split(": ")
    vals = vals.split(" or ")
    ranges = []

    for val in vals:
        start,end = val.split("-")
        ranges.append([int(start), int(end)])

    return (name, ranges)

f = open("day-16-input.txt", "r")
input = f.read().split("\n\n")

# parse rules
rules = input[0].splitlines()
rules = dict(map(parseRule, rules))

# parse nearby tickets
nearbyTickets = input[2].splitlines()
# remove description line
nearbyTickets.pop(0)
nearbyTickets = list(map(lambda t: list(map(int, t.split(','))), nearbyTickets))

# calculate error rate
errorRate = 0
for t in nearbyTickets:
    for val in t:
        isValid = False
        for r in rules.values():
            for start,end in r:
                # found valid rule for value
                if val >= start and val <= end:
                    isValid = True
                    break

        if not isValid:
            errorRate += val

print(errorRate)

f.close()
