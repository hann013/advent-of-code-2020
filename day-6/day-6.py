### ***** Advent of Code 2020 - Day 6 ***** ###

def getYesAnswers(group):
    # get array of letters, then convert to set to return unique letters
    answers = group.split("\n")
    unique = [letter for a in answers for letter in a]
    return set(unique)

def getEveryoneYesAnswers(group):
    answers = group.split("\n")
    # convert answers to sets of letters so we can get the intersection of sets
    answers = list(map(set, answers))
    everyone = answers[0]
    for a in answers[1:]:
        # ignore empty sets
        if not len(a) == 0:
            everyone = everyone.intersection(a)
    return everyone

f = open("day-6-input.txt", "r")
input = f.read()
groups = input.split("\n\n")

# Part 1
answers = list(map(getYesAnswers, groups))

sum = 0
for a in answers:
    sum += len(a)
print(sum)

# Part 2
answers = list(map(getEveryoneYesAnswers, groups))

sum = 0
for a in answers:
    sum += len(a)
print(sum)

f.close()
