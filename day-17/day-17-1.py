### ***** Advent of Code 2020 - Day 17 Part 1 ***** ###
import copy

f = open("day-17-input.txt", "r")
input = f.readlines()
input = [list(map(lambda i: list(i.strip()), input))]

active = "#"
inactive = "."

# expand grid to +1 length in all directions
def expand(oldGrid):
    zl, yl, xl = len(oldGrid) + 2, len(oldGrid[0]) + 2, len(oldGrid[0][0]) + 2
    newGrid = []

    # prepend and append empty slices to existing slices
    emptySlice = [list(inactive * xl) for i in range (yl)]
    newGrid.append(emptySlice)

    # add new rows/cols
    for slice in oldGrid:
        newRows = []
        emptyRow = list(inactive * xl)

        # prepend and append empty rows to existing rows
        newRows.append(emptyRow)
        for row in slice:
            # prepend and append empty spots to existing spots
            newRows.append([inactive] + row + [inactive])
        newRows.append(emptyRow)
        newGrid.append(newRows)

    newGrid.append(emptySlice)
    return newGrid

def getNumActiveNeighbours(grid, coords):
    zl, yl, xl = len(grid), len(grid[0]), len(grid[0][0])
    z, y, x = coords
    count = 0

    for nz in range(max(0, z-1), min(z+2, zl)):
        for ny in range(max(0, y-1), min(y+2, yl)):
            for nx in range(max(0, x-1), min(x+2, xl)):
                if not (nz == z and ny == y and nx == x):
                    if grid[nz][ny][nx] == active:
                        count += 1
    return count

def countNumActive(grid):
    count = 0
    for slice in grid:
        for row in slice:
            for element in row:
                if element == active:
                    count += 1
    return count

oldGrid = input
for i in range(1, 7):
    oldGrid = expand(oldGrid)
    newGrid = copy.deepcopy(oldGrid)

    for zi,slice in enumerate(newGrid):
        for yi,row in enumerate(slice):
            for xi,element in enumerate(row):
                numActive = getNumActiveNeighbours(oldGrid, (zi, yi, xi))
                if element == active:
                    if numActive < 2 or numActive > 3:
                        newGrid[zi][yi][xi] = inactive
                elif element == inactive:
                    if numActive == 3:
                        newGrid[zi][yi][xi] = active
    oldGrid = newGrid

print(countNumActive(oldGrid))

f.close()
