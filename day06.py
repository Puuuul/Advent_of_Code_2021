from collections import deque


def method1():
    file1 = open("input files/day6.txt")
    s = file1.readline()
    arr = s.split(",")
    fishcount = deque([0 for i in range(9)])
    for fish in arr:
        fishcount[int(fish)] += 1
    for x in range(256):
        fishcount.rotate(-1)
        fishcount[6] += fishcount[8]
    print(sum(fishcount))


method1()
