### ***** Advent of Code 2020 - Day 13 Part 1 ***** ###
import copy

f = open("day-13-input.txt", "r")
input = f.readlines()

departure = int(input[0])
buses = input[1].strip().split(",")
buses = list(filter(lambda b: b != "x", buses))
buses = list(map(int, buses))

deps = copy.copy(buses)

for i,b in enumerate(buses):
    # Get the first bus departure time after the required departure timestamp
    d = departure // b
    r = departure % b
    deps[i] = b * d if r == 0 else b * (d + 1)

smallest = min(deps)
i = deps.index(smallest)

print((smallest - departure) * buses[i])

f.close()
