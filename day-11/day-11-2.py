### ***** Advent of Code 2020 - Day 11 Part 2 ***** ###
import copy

f = open("day-11-input.txt", "r")
input = f.readlines()
input = list(map(lambda x: list(x.strip()), input))

floor = "."
occupied = "#"
empty = "L"

rowLength = len(input[0])
colLength = len(input)

def isValidSeat(row, col):
    return row >= 0 and row < colLength and col >= 0 and col < rowLength

def findSeatInDirection(seats, row, ro, col, co):
    while isValidSeat(row, col):
        row += ro
        col += co

        if isValidSeat(row, col):
            s = seats[row][col]
            if s != floor:
                return s

    return "."

def noAdjacentOccupiedSeats(seats, row, col):
    for ro in range(-1, 2):
        for co in range (-1, 2):
            if not (ro == 0 and co == 0):
                s = findSeatInDirection(seats, row, ro, col, co)
                if s == occupied:
                    return False
    return True

def fiveOrMoreOccupiedSeats(seats, row, col):
    numOccupied = 0

    for ro in range(-1, 2):
        for co in range (-1, 2):
            if not (ro == 0 and co == 0):
                s = findSeatInDirection(seats, row, ro, col, co)
                if s == occupied:
                    numOccupied += 1

    return numOccupied >= 5

numOccupied = 0
old = input

while True:
    new = copy.deepcopy(old)

    for row in range(colLength):
        for col in range(rowLength):
            seat = old[row][col]
            if seat == empty and noAdjacentOccupiedSeats(old, row, col):
                new[row][col] = occupied
            elif seat == occupied and fiveOrMoreOccupiedSeats(old, row, col):
                new[row][col] = empty

    o = 0
    for row in new:
        for seat in row:
            if seat == occupied:
                o += 1

    if o == numOccupied:
        break
    else:
        numOccupied = o
        old = new

print(numOccupied)

f.close()
