def method1():
    file1 = open("input files/day1.txt")
    Lines = file1.readlines()
    ints = []
    for line in Lines:
        line.strip()
        ints += [int(line)]
    count = 0

    for x in range(len(ints)):
        if ints[x] > ints[x-1]:
            count += 1

    print(count)


def method2():
    file2 = open("input files/day1txt")
    Lines = file2.readlines()
    ints = []
    for line in Lines:
        line.strip()
        ints += [int(line)]
    count = 0

    for x in range(len(ints)-2):
        first = ints[x-1]+ints[x]+ints[x+1]
        second = ints[x]+ints[x+1]+ints[x+2]
        if first < second:
            count += 1

    print(count)


method1()
method2()