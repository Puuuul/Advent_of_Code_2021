import sys
sys.setrecursionlimit(10000)


def paths(point, arr, conns, small):
    count = 0
    if point == "end":
        return 1
    if point[0].islower():
        if point in arr:
            if not point == "start" and small:
                small = False
            else:
                return 0
    arr.append(point)
    for conn in conns[point]:
        count += paths(conn, arr.copy(), conns, small)
    return count


def method1():
    conns = {}
    file1 = open("input files/day12.txt")
    lines = file1.readlines()
    for line in lines:
        line = line.strip()
        split = line.split("-")
        for x in range(2):
            if split[0+x] not in conns:
                conns[split[0+x]] = [split[1-x]]
            else:
                conns[split[0+x]].append(split[1-x])
    small = True
    arr = []
    print(paths("start", arr, conns, small))


method1()
