def count(lines, i):
    x0 = 0
    x1 = 0
    for line in lines:
        if line[i] == "0":
            x0 += 1
        else:
            x1 += 1
    if x0 > x1:
        return 0
    elif x1 > x0:
        return 1
    else:
        return -1


def method1():
    file1 = open("input files/day03.txt")
    lines = file1.readlines()
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
    gamma = ""
    epsilon = ""
    for x in range(len(lines[0])):
        if count(lines, x) == 1:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(int(gamma, 2)*int(epsilon, 2))


def oxygen(lines, i):
    out = []
    if count(lines, i) == 0:
        for line in lines:
            if line[i] == "0":
                out.append(line)
    else:
        for line in lines:
            if line[i] == "1":
                out.append(line)
    return out


def co2(lines, i):
    arr = count(lines, i)
    out = []
    if count(lines, i) == 0:
        for line in lines:
            if line[i] == "1":
                out.append(line)
    else:
        for line in lines:
            if line[i] == "0":
                out.append(line)
    return out


def method2():
    file1 = open("input files/day03.txt")
    lines = file1.readlines()
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
    linesO2 = lines
    linesCO = lines
    for x in range(len(lines[0])):
        linesO2 = oxygen(linesO2, x)
        if len(linesO2) == 1:
            break
    for x in range(len(lines[0])):
        linesCO = co2(linesCO, x)
        if len(linesCO) == 1:
            break
    print(int(linesO2[0], 2)*int(linesCO[0], 2))


method1()
method2()
