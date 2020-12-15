### ***** Advent of Code 2020 - Day 14 Part 1 ***** ###

# convert value into padded 8-bit string
def convertToBin(val):
    # convert to binary, then to string, and remove '0b'
    val = str(bin(int(val)))[2:]
    # pad with 0s
    for i in range(36-len(val)):
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

f = open("day-14-input.txt", "r")
input = f.readlines()
input = list(map(lambda i: i.strip().split(" = "), input))

curMask = ""
addresses = dict()

for i in input:
    key = i[0]
    if key == "mask":
        curMask = i[1]
    else:
        # get mem address
        i1 = key.find("[") + 1
        i2 = key.find("]")
        addr = int(i[0][i1:i2])

        # convert value to binary and apply mask
        val = convertToBin(i[1])
        for i,l in enumerate(curMask):
            if l == "0" or l == "1":
                val[i] = l

        # convert value back to dec and store
        addresses[addr] = convertToDec("".join(val))

print(sum(addresses.values()))
