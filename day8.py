def method1():
    file1 = open("input files/day8.txt")
    lines = file1.readlines()
    count = 0
    a = [2, 3, 4, 7]
    for line in lines:
        s = line.split(" | ")[1]
        arr = s.split()
        for let in arr:
            let = len(let)
            if let in a:
                count += 1
    print(count)


def decypher(arr):
    out = ["" for i in range(10)]
    for num in arr:
        if len(num) == 2:
            out[1] = num
            continue
        if len(num) == 3:
            out[7] = num
            continue
        if len(num) == 4:
            out[4] = num
            continue
        if len(num) == 7:
            out[8] = num
            continue
    for num in out:
        if num in arr:
            arr.remove(num)
    for num in arr:
        if len(num) == 6:
            b = False
            for i in out[7]:
                if i not in num:
                    b = True
                    break
            for i in out[4]:
                if i not in num:
                    b = True
                    break
            if not b:
                out[9] = num
                arr.remove(num)
                break
    for num in arr:
        if len(num) == 6:
            b = False
            for i in out[7]:
                if i not in num:
                    out[6] = num
                    b = True
                    break
            if b:
                continue
            out[0] = num
    for num in out:
        if num in arr:
            arr.remove(num)
    for num in arr:
        if len(num) == 5:
            b = False
            for i in out[1]:
                if i not in num:
                    b = True
                    break
            if b:
                continue
            out[3] = num
            arr.remove(num)
            break
    for num in arr:
        count = 0
        for i in num:
            if i not in out[9]:
                count += 1
        if count == 1:
            out[2] = num
        else:
            out[5] = num
    return out


def method2():
    file1 = open("input files/day8.txt")
    lines = file1.readlines()
    final = 0
    for line in lines:
        out = ""
        s = line.split(" | ")
        arr = s[0].split()
        numbers = decypher(arr)
        digits = s[1].split()
        for digit in digits:
            for num in numbers:
                b = False
                for i in num:
                    if i not in digit:
                        b = True
                        break
                for i in digit:
                    if i not in num:
                        b = True
                        break
                if b:
                    continue
                out += str(numbers.index(num))
                break
        final += int(out)
    print(final)


method1()
method2()
