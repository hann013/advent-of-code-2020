### ***** Advent of Code 2020 - Day 17 Part 2 ***** ###
import copy

f = open("day-17-input.txt", "r")
input = f.readlines()
input = [[list(map(lambda i: list(i.strip()), input))]]

active = "#"
inactive = "."

# expand cube to +1 length in all directions
def expand(oldCube):
    wl, zl, yl, xl = len(oldCube) + 2, len(oldCube[0]) + 2, len(oldCube[0][0]) + 2, len(oldCube[0][0][0]) + 2
    newCube = []

    # prepend and append empty grids to existing grids
    emptyGrid = [[list(inactive * xl) for i in range (yl)] for i in range(zl)]
    newCube.append(emptyGrid)

    for grid in oldCube:
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
    newCube.append(emptyGrid)
    return newCube

def getNumActiveNeighbours(cube, coords):
    wl, zl, yl, xl = len(cube), len(cube[0]), len(cube[0][0]), len(cube[0][0][0])
    w, z, y, x = coords
    count = 0

    for nw in range(max(0, w-1), min(w+2, wl)):
        for nz in range(max(0, z-1), min(z+2, zl)):
            for ny in range(max(0, y-1), min(y+2, yl)):
                for nx in range(max(0, x-1), min(x+2, xl)):
                    if not (nw == w and nz == z and ny == y and nx == x):
                        if cube[nw][nz][ny][nx] == active:
                            count += 1
    return count

def countNumActive(cube):
    count = 0
    for grid in cube:
        for slice in grid:
            for row in slice:
                for element in row:
                    if element == active:
                        count += 1
    return count

oldCube = input
for i in range(1,7):
    oldCube = expand(oldCube)
    newCube = copy.deepcopy(oldCube)

    for wi,grid in enumerate(oldCube):
        for zi,slice in enumerate(grid):
            for yi,row in enumerate(slice):
                for xi,element in enumerate(row):
                    numActive = getNumActiveNeighbours(oldCube, (wi, zi, yi, xi))
                    if element == active:
                        if numActive < 2 or numActive > 3:
                            newCube[wi][zi][yi][xi] = inactive
                    elif element == inactive:
                        if numActive == 3:
                            newCube[wi][zi][yi][xi] = active
    oldCube = newCube

print(countNumActive(oldCube))

f.close()
