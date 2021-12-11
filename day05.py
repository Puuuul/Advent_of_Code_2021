import numpy


def makeline1(grid, start, end):
    s = ""
    if start[1] > end[1]:
        s += "N"
    if start[1] < end[1]:
        s += "S"
    if start[0] < end[0]:
        s += "O"
    if start[0] > end[0]:
        s += "W"
    if s == "N":
        for x in range(start[1] - end[1] + 1):
            grid[start[0]][start[1] - x] += 1
    if s == "S":
        for x in range(end[1] - start[1] + 1):
            grid[start[0]][start[1] + x] += 1
    if s == "O":
        for x in range(end[0] - start[0] + 1):
            grid[start[0] + x][start[1]] += 1
    if s == "W":
        for x in range(start[0] - end[0] + 1):
            grid[start[0] - x][start[1]] += 1
    return grid


def makeline2(grid, start, end):
    s = ""
    if start[1] > end[1]:
        s += "N"
    if start[1] < end[1]:
        s += "S"
    if start[0] < end[0]:
        s += "O"
    if start[0] > end[0]:
        s += "W"
    if not ((len(s) > 1) and (abs(start[0] - end[0]) != abs(start[1] - end[1]))):
        x = 0
        y = 0
        if s.__contains__("N"):
            y = -1
        if s.__contains__("S"):
            y = 1
        if s.__contains__("O"):
            x = 1
        if s.__contains__("W"):
            x = -1
        num = abs(start[0] - end[0])
        if num == 0:
            num = abs(start[1] - end[1])
        for i in range(num + 1):
            grid[start[0] + (x * i)][start[1] + (y * i)] += 1
    return grid


def method1():
    file1 = open("input files/day05.txt")
    lines = file1.readlines()
    start = [[0 for c in range(2)] for r in range(len(lines))]
    end = [[0 for c in range(2)] for r in range(len(lines))]
    length = 0
    height = 0
    for x in range(len(lines)):
        line = lines[x].strip()
        arr = line.split(" -> ")
        start[x] = arr[0].split(",")
        end[x] = arr[1].split(",")
        for n in range(2):
            start[x][n] = int(start[x][n])
            end[x][n] = int(end[x][n])
        if start[x][0] > length:
            length = start[x][0]
        if end[x][0] > length:
            length = end[x][0]
        if start[x][1] > height:
            height = start[x][1]
        if end[x][1] > height:
            height = end[x][1]
    print(length)
    print(height)
    grid = [[0 for c in range(height + 1)] for r in range(length + 1)]
    for x in range(len(start)):
        grid = makeline1(grid, start[x], end[x])
    count = 0
    for col in grid:
        for num in col:
            if num > 1:
                count += 1
    print(count)
    grid = [[0 for c in range(height + 1)] for r in range(length + 1)]
    for x in range(len(start)):
        grid = makeline2(grid, start[x], end[x])
    count = 0
    for col in grid:
        for num in col:
            if num > 1:
                count += 1
    print(numpy.transpose(grid))
    print(count)


method1()
