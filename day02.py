def method1():
    file1 = open("input files/day02.txt")
    lines = file1.readlines()
    arr = [[], []]
    for line in lines:
        s = line.split()
        arr[0].append(s[0])
        arr[1].append(int(s[1]))
    hor = 0
    dep = 0

    for x in range(len(arr[0])):
        if arr[0][x] == "forward":
            hor += arr[1][x]
        elif arr[0][x] == "down":
            dep += arr[1][x]
        elif arr[0][x] == "up":
            dep -= arr[1][x]

    print(hor * dep)


def method2():
    file2 = open("input files/day02.txt")
    lines = file2.readlines()
    arr = [[], []]
    for line in lines:
        s = line.split()
        arr[0].append(s[0])
        arr[1].append(int(s[1]))
    hor = 0
    dep = 0
    aim = 0

    for x in range(len(arr[0])):
        if arr[0][x] == "forward":
            hor += arr[1][x]
            dep += arr[1][x] * aim
        elif arr[0][x] == "down":
            aim += arr[1][x]
        elif arr[0][x] == "up":
            aim -= arr[1][x]

    print(hor * dep)


method1()
method2()
