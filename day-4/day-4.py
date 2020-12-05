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
                    isValid = False
                    break
            elif key == "iyr":
                year = int(val)
                if year < 2010 or year > 2020:
                    isValid = False
                    break
            elif key == "eyr":
                year = int(val)
                if year < 2020 or year > 2030:
                    isValid = False
                    break
            elif key == "hgt":
                if "cm" in val:
                    height = int(val.split("cm")[0])
                    if height < 150 or height > 193:
                        isValid = False
                        break
                elif "in" in val:
                    height = int(val.split("in")[0])
                    if height < 59 or height > 76:
                        isValid = False
                        break
                else:
                    isValid = False
                    break
            elif key == "hcl":
                # # followed by exactly 6 characters 0-9 or a-f
                match = re.search("^#([0-9]|[a-f]){6}$", val)
                if not match:
                    isValid = False
                    break
            elif key == "ecl":
                if not val in validEyeColors:
                    isValid = False
                    break
            elif key == "pid":
                # Check that it's a valid number
                try:
                    int(val)
                except ValueError:
                    isValid = False
                    break
                if len(val) != 9:
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
