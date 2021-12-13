def fold(grid, ori, coord):
    if ori == "y":
        list1 = grid[:coord]
        list2 = grid[coord+1:]
        list2.reverse()
        for y in range(len(list2)):
            for x in range(len(list2[0])):
                list1[y][x] += list2[y][x]
    else:
        list1 = []
        list2 = []
        for y in grid:
            list1.append(y[:coord])
            list2.append(y[coord+1:])
        for x in range(len(list2)):
            list2[x].reverse()
        for y in range(len(list2)):
            for x in range(len(list2[0])):
                list1[y][x] += list2[y][x]
    return list1


def method():
    file1 = open("input files/day13.txt")
    lines = file1.readlines()
    f = False
    arr = [[], []]
    folds = []
    for line in lines:
        line = line.strip()
        if line == "":
            f = True
        elif not f:
            split = line.split(",")
            for x in range(2):
                arr[x].append(int(split[x]))
        else:
            folds.append(line.split()[2].split("="))
    grid = [[0 for i in range(max(arr[0])+1)] for j in range(max(arr[1])+1)]
    for x in range(len(arr[0])):
        grid[arr[1][x]][arr[0][x]] = 1
    grid = fold(grid, folds[0][0], int(folds[0][1]))
    count = 0
    for y in grid:
        for x in y:
            if x > 0:
                count += 1
    print(count)
    grid = [[0 for i in range(max(arr[0]) + 1)] for j in range(max(arr[1]) + 1)]
    for x in range(len(arr[0])):
        grid[arr[1][x]][arr[0][x]] = 1
    for ele in folds:
        grid = fold(grid, ele[0], int(ele[1]))
    outs = ["" for i in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] > 0:
                outs[y] += "#"
            else:
                outs[y] += "."
    for x in outs:
        print(x)


method()
