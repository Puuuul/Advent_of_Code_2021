def method1():
    file1 = open("input files/day09.txt")
    lines = file1.readlines()
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
    pr = 0
    out = []
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if not x == 0:
                if lines[x-1][y] <= lines[x][y]:
                    continue
            if not x == len(lines)-1:
                if lines[x+1][y] <= lines[x][y]:
                    continue
            if not y == 0:
                if lines[x][y-1] <= lines[x][y]:
                    continue
            if not y == len(lines[0])-1:
                if lines[x][y+1] <= lines[x][y]:
                    continue
            pr += int(lines[x][y]) + 1
            out.append((x, y))
    print(pr)
    return out


def discover(x, y, grid, count):
    count += 1
    grid[x][y] = 9
    if x > 0:
        if not grid[x-1][y] == 9:
            grid, count = discover(x-1, y, grid, count)
    if y > 0:
        if not grid[x][y-1] == 9:
            grid, count = discover(x, y-1, grid, count)
    if x < len(grid)-1:
        if not grid[x+1][y] == 9:
            grid, count = discover(x+1, y, grid, count)
    if y < len(grid[0])-1:
        if not grid[x][y+1] == 9:
            grid, count = discover(x, y+1, grid, count)
    return grid, count


def method2():
    file1 = open("input files/day09.txt")
    lines = file1.readlines()
    grid = [[0 for i in range(len(lines[0])-1)] for j in range(len(lines))]
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
        for i in range(len(lines[x])):
            grid[x][i] = int(lines[x][i])
    deeps = method1()
    counts = []
    for deep in deeps:
        grid, count = discover(deep[0], deep[1], grid, 0)
        counts.append(count)
    counts = (sorted(counts, reverse=True)[:3])
    print(counts[0]*counts[1]*counts[2])


method2()
