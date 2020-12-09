### ***** Advent of Code 2020 - Day 7 ***** ###

# Parse each bag's contents into {num: [number of content bags], color: [color of content bag]}
def parseRule(rule):
    rule = rule.split("bags contain ")
    color = rule[0].strip()
    contents = rule[1]

    if "no other bags" in contents:
        return [color, []]

    contents = contents.split(", ")
    bags = []
    for bag in contents:
        words = bag.split(" ")
        bags.append({"num": int(words[0]), "color": words[1] + " " + words[2]})
    return [color, bags]

# Recursively find bags that contain shiny gold bags
def findShinyGoldBag(rules, color):
    bags = list(map(lambda b: b["color"], rules[color]))
    if "shiny gold" in bags:
        return True
    for c in bags:
        result = findShinyGoldBag(rules, c)
        if result == True:
            return True
    return False

# Recursively count the number of bags
def countNumShinyGoldBags(rules, count, bag, numCurrentBag):
    bags = rules[bag["color"]]
    for b in bags:
        n = numCurrentBag * b["num"]
        count[0] = count[0] + n
        countNumShinyGoldBags(rules, count, b, n)

f = open("day-7-input.txt", "r")
input = f.readlines()

rules = {}
for rule in input:
    color, bags = parseRule(rule)
    rules[color] = bags

# Part 1
num = 0
for color in rules.keys():
    if findShinyGoldBag(rules, color) == True:
        num += 1
print(num)

# Part 2
# Declare this value in a list so it can be passed by reference
count = [0]
bags = rules["shiny gold"]
for bag in bags:
    n = bag["num"]
    count[0] = count[0] + n
    countNumShinyGoldBags(rules, count, bag, n)
print(count[0])

f.close()
