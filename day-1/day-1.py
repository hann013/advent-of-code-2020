### ***** Advent of Code 2020 - Day 1 ***** ###

f = open("day-1-input.txt", "r")
input = f.read().splitlines()
nums = list(map(lambda n: int(n), input))
nums.sort()
length = len(nums)
target = 2020

# Part 1
i1 = 0
i2 = 1
while i1 < length and i2 < length:
    num1 = nums[i1]
    num2 = nums[i2]
    sum = num1 + num2

    if sum == target: # found the solution
        print(num1 * num2)
        break
    elif sum < target: # sum too small, so increment higher num unless it's at max
        if i2 == length - 1:
            i1 += 1
            i2 = i1+1
        else:
            i2 += 1
    elif sum > target: # sum too large, so increment lower num and reset higher num
        i1 += 1
        i2 = i1+1

# Part 2
i1 = 0
i2 = 1
i3 = 2
while i1 < length and i2 < length and i3 < length:
    num1 = nums[i1]
    num2 = nums[i2]
    num3 = nums[i3]
    sum = num1 + num2 + num3

    if sum == target: # found the solution
        print(num1 * num2 * num3)
        break
    elif sum < target: # sum too small, so increment third number
        if i3 == length - 1: # can't increment third num anymore, so increment second num
            i2 += 1
        else:
            i3 += 1
    elif sum > target:
        if num2 + num3 > target: # two larger nums are too big, so increment lowest num and reset others
            i1 += 1
            i2 = i1+1
        else: # increment second num but reset third num
            i2 += 1
        i3 = i2+1

f.close()
