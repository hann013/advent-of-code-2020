### ***** Advent of Code 2020 - Day 9 ***** ###

f = open("day-9-input.txt", "r")
input = f.readlines()

# convert each line to int
input = list(map(int, input))

length = 25
result = 0
for i,target in enumerate(input[length:], start=length):
    # get and sort preamble (previous 25 numbers)
    preamble = input[i-length:i]
    preamble.sort()

    i1 = 0
    i2 = 1
    noSum = True

    # search for numbers in preamble that sum to the target
    while i1 < length and i2 < length:
        num1 = preamble[i1]
        num2 = preamble[i2]
        sumOfNums = num1 + num2

        if sumOfNums == target: # found a sum from previous 25 numbers
            noSum = False
            break
        elif sumOfNums < target: # sum too small, so increment higher num unless it's at max
            if i2 == length - 1:
                i1 += 1
                i2 = i1+1
            else:
                i2 += 1
        elif sumOfNums > target: # sum too large, so increment lower num and reset higher num
            i1 += 1
            i2 = i1+1

    # found result if no sum from numbers in preamble
    if noSum:
        result = target
        break

print(result)

# Part 2
target = result
nums = []
for i in range(len(input)):
    arraySum = sum(nums)

    # found target, so return result
    if arraySum == target:
        nums.sort()
        # result is sum of lowest and highest number
        print(nums[0] + nums[len(nums)-1])
        break
    elif arraySum < target:
        # haven't reached target yet, so add new number to array
        nums.append(input[i])
    elif arraySum > target:
        # we can safely pop all numbers until we're under the target again
        while arraySum > target:
            nums.pop(0)
            arraySum = sum(nums)

        # check to see if we've hit the target before adding new number to array
        if arraySum == target:
            nums.sort()
            print(nums[0] + nums[len(nums)-1])
            break
        else:
            nums.append(input[i])

f.close()
