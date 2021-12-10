def method1():
    file1 = open("input files/day10.txt")
    lines = file1.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        arr = []
        for char in line:
            if char == ")":
                if not arr.pop() == "(":
                    count += 3
                    break
            elif char == "]":
                if not arr.pop() == "[":
                    count += 57
                    break
            elif char == "}":
                if not arr.pop() == "{":
                    count += 1197
                    break
            elif char == ">":
                if not arr.pop() == "<":
                    count += 25137
                    break
            else:
                arr.append(char)
    print(count)


def method2():
    file1 = open("input files/day10.txt")
    lines = file1.readlines()
    delete = []
    out = []
    count = 0
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
        arr = []
        for char in lines[x]:
            if char == ")":
                if not arr.pop() == "(":
                    delete.append(x)
                    break
            elif char == "]":
                if not arr.pop() == "[":
                    delete.append(x)
                    break
            elif char == "}":
                if not arr.pop() == "{":
                    delete.append(x)
                    break
            elif char == ">":
                if not arr.pop() == "<":
                    delete.append(x)
                    break
            else:
                arr.append(char)
        out.append(arr)
    delete.reverse()
    for ele in delete:
        del out[ele]
    arr = []
    for line in out:
        x = 0
        line.reverse()
        for char in line:
            if char == "(":
                x = x * 5 + 1
            elif char == "[":
                x = x * 5 + 2
            elif char == "{":
                x = x * 5 + 3
            else:
                x = x * 5 + 4
        arr.append(x)
    print(sorted(arr)[int((len(arr) - 1)/2)])


method1()
method2()
