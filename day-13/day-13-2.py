### ***** Advent of Code 2020 - Day 13 Part 2 ***** ###

f = open("day-13-input.txt", "r")
input = f.readlines()
input = input[1].strip().split(",")

# store offset
buses = []
offsets = []
offset = 0
for i,b in enumerate(input):
    if b != "x":
        buses.append(int(b))
        offsets.append(offset)
    offset -= 1

print(buses)
print(offsets)

# Extended Euclidean algorithm to find the inverse of Nn mod n
def findInverse(Nn, n):
    if n == 1:
        return 1

    n0 = n
    s0, s1 = 0, 1

    while Nn > 1:
        q = n // Nn
        Nn, n = n % Nn, Nn
        s0, s1 = s1, s0 - s1 * q

    return s1 % n0

# Chinese Remainder Theorem
N = 1
for b in buses:
    N *= b

sum = 0
for n,a in zip(buses, offsets):
    Nn = N // n
    sum += a * findInverse(Nn, n) * Nn

print(sum % N)

f.close()
