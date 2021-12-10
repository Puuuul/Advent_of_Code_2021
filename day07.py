import sys
file1 = open("input files/day7.txt")
s = file1.readline()
numbers = s.split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


def method1():
    out = sys.maxsize
    for i in range(max(numbers)):
        x = 0
        for number in numbers:
            x += abs(i-number)
        if x < out:
            out = x
    print(out)


def method2():
    out = sys.maxsize
    for i in range(max(numbers)):
        x = 0
        for number in numbers:
            for y in range(abs(i - number)):
                x += y+1
        if x < out:
            out = x
    print(out)


method1()
method2()
