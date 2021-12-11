def flash(x, y, grid, count):
    count += 1
    grid[x][y] = -1
    for i in range(3):
        for j in range(3):
            if 0 <= x - 1 + i < 10 and 0 <= y - 1 + j < 10:
                if grid[x - 1 + i][y - 1 + j] >= 0:
                    grid[x - 1 + i][y - 1 + j] += 1
                    if grid[x - 1 + i][y - 1 + j] > 9:
                        grid, count = flash(x - 1 + i, y - 1 + j, grid, count)
    return grid, count


def method1():
    file1 = open("input files/day11.txt")
    lines = file1.readlines()
    grid = [[0 for x in range(10)] for y in range(10)]
    for x in range(10):
        lines[x] = lines[x].strip()
        for y in range(10):
            grid[x][y] = int(lines[x][y])
    count = 0
    c = 0
    while True:
        c += 1
        for x in range(10):
            for y in range(10):
                if grid[x][y] >= 0:
                    grid[x][y] += 1
                    if grid[x][y] > 9:
                        grid, count = flash(x, y, grid, count)
        flashes = 0
        for x in range(10):
            for y in range(10):
                if grid[x][y] == -1:
                    grid[x][y] = 0
                    flashes += 1
        print(flashes)
        if flashes == 100:
            print(c)
            break
    print(count)


method1()
