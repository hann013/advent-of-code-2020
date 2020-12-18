### ***** Advent of Code 2020 - Day 16 ***** ###
import copy

def parseRule(rule):
    name, vals = rule.split(": ")
    vals = vals.split(" or ")
    ranges = []

    for val in vals:
        start,end = val.split("-")
        ranges.append([int(start), int(end)])

    return (name, ranges)

f = open("day-16-input.txt", "r")
input = f.read()
input = input.split("\n\n")

# parse rules
rules = input[0].splitlines()
rules = dict(map(parseRule, input[0].splitlines()))

# parse nearby tickets
nearbyTickets = input[2].splitlines()
# remove description line
nearbyTickets.pop(0)
nearbyTickets = list(map(lambda t: list(map(int, t.split(','))), nearbyTickets))

# discard invalid tickets
validTickets = copy.deepcopy(nearbyTickets)
for i,t in enumerate(nearbyTickets):
    for val in t:
        isValid = False
        for rule in rules.values():
            for start,end in rule:
                if val >= start and val <= end:
                    isValid = True
                    break

        if not isValid:
            validTickets[i] = None
            break
validTickets = [t for t in validTickets if not t is None]

# get all possible fields per position
fields = dict()
for t in validTickets:
    for i,val in enumerate(t):
        # keep track of all possible rules that this value passes
        possible = set()
        for name,rule in rules.items():
            for start,end in rule:
                if val >= start and val <= end:
                    # found a possible passing rule
                    possible.add(name)
                    break

        if not fields.get(i):
            fields[i] = possible
        else:
            # compare against previous values at this position to filter out possibilities
            fields[i] = fields[i].intersection(possible)

# sort fields by number of possibilities
fields = sorted(fields.items(), key=lambda f: len(f[1]))

# discard possibilities by comparing sets
for i,tuple in enumerate(fields):
    f1 = tuple[1]
    for k,f2 in fields:
        if len(f2) < len(f1):
            f1 = f1 - f2
    fields[i] = (tuple[0], f1)

# sort fields back by array index
fields = sorted(fields, key=lambda field: field[0])
fields = list(map(lambda field: field[1].pop(), fields))

# parse my ticket
myTicket = input[1].splitlines()[1]
myTicket = list(map(int, myTicket.split(',')))

# calculate result
result = 1
for i,field in enumerate(fields):
    if "departure" in field:
        result *= myTicket[i]

print(result)

f.close()
