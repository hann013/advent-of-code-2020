### ***** Advent of Code 2020 - Day 14 Part 2 ***** ###
import copy

# convert value into padded binary string
def convertToBin(val):
    # convert to binary, then to string, and remove '0b'
    val = str(bin(int(val)))[2:]
    # pad with 0s
    for i in range(maskLen-len(val)):
        val = "0" + val
    return list(val)

def convertToDec(val):
    result = 0
    base = 1
    for i in reversed(range(len(val))):
        if val[i] == "1":
            result += base
        base *= 2
    return result

def storeValues(addr, val):
    storeAllPossible(addr, 0, val)

def storeAllPossible(addr, curIndex, val):
    # reached the end, so store val in address
    if curIndex == len(addr):
        a = convertToDec("".join(addr))
        addresses[a] = val
    else:
        for i in range(curIndex, len(addr)):
            if addr[i] == "X":
                c = copy.copy(addr)
                c[i] = "0"
                storeAllPossible(c, i+1, val)
                c[i] = "1"
                storeAllPossible(c, i+1, val)
                break
            elif i == len(addr) - 1:
                a = convertToDec("".join(addr))
                addresses[a] = val

f = open("day-14-input.txt", "r")
input = f.readlines()
input = list(map(lambda i: i.strip().split(" = "), input))
maskLen = 36

curMask = ""
addresses = dict()

for line in input:
    key = line[0]
    if key == "mask":
        curMask = line[1]
    else:
        # get mem address
        i1 = key.find("[") + 1
        i2 = key.find("]")
        addr = int(line[0][i1:i2])

        # convert address to binary and apply mask
        addr = convertToBin(addr)
        for i,l in enumerate(curMask):
            if l == "1" or l == "X":
                addr[i] = l
        storeValues(addr, int(line[1]))

print(sum(addresses.values()))
