### ***** Advent of Code 2020 - Day 4 ***** ###
import re

def getPassportFields(passport):
    fields = []
    lines = passport.split("\n")
    for data in lines:
        p = data.split(" ")
        for field in p:
            field = field.split(":")
            if len(field) == 2:
                fields.append(field)
    return fields

def isValidPassport(fields):
    numFields = 0;
    for field in fields:
        if field[0] in requiredFields:
            numFields += 1
    return numFields == len(requiredFields)

# Part 1
def getNumValidPassportsOne(passports):
    numValid = 0;
    for fields in passports:
        if isValidPassport(fields):
            numValid += 1
    return numValid

# Part 2
def getNumValidPassportsTwo(passports):
    numValid = 0;
    for fields in passports:
        if not isValidPassport(fields):
            continue

        isValid = True
        for field in fields:
            key, val = field
            if key == "byr":
                year = int(val)
                if year < 1920 or year > 2002:
                    print("invalid byr", year)
                    isValid = False
                    break
            elif key == "iyr":
                year = int(val)
                if year < 2010 or year > 2020:
                    print("invalid iyr", year)
                    isValid = False
                    break
            elif key == "eyr":
                year = int(val)
                if year < 2020 or year > 2030:
                    print("invalid eyr", year)
                    isValid = False
                    break
            elif key == "hgt":
                if "cm" in val:
                    height = int(val.split("cm")[0])
                    if height < 150 or height > 193:
                        print("invalid hgt cm", height)
                        isValid = False
                        break
                elif "in" in val:
                    height = int(val.split("in")[0])
                    if height < 59 or height > 76:
                        print("invalid hgt in", height)
                        isValid = False
                        break
                else:
                    print("invalid hgt", height)
                    isValid = False
                    break
            elif key == "hcl":
                match = re.search("^#([0-9]|[a-f]){6}$", val)
                if not match:
                    print("invalid hcl", repr(val))
                    isValid = False
                    break
            elif key == "ecl":
                if not val in validEyeColors:
                    print("invalid ecl", val)
                    isValid = False
                    break
            elif key == "pid":
                try:
                    int(val)
                except ValueError:
                    print("invalid pid", val)
                    isValid = False
                    break
                if len(val) != 9:
                    print("invalid pid", val)
                    isValid = False
                    break

        if isValid:
            numValid += 1
    return numValid

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

f = open("day-4-input.txt", "r")
input = f.read()
passports = input.split("\n\n")

fields = list(map(getPassportFields, passports))
print(getNumValidPassportsOne(fields))
print(getNumValidPassportsTwo(fields))
