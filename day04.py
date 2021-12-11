def checkwon(board):
    for line in board:
        if line.count(-1) == 5:
            for line in board:
                print(line)
            return True
    for c in range(5):
        x = 0
        for r in range(5):
            x -= int(board[r][c])
        if x == 5:
            for line in board:
                print(line)
            return True
    return False


def method1():
    file1 = open("input files/day04.txt")
    lines = file1.readlines()
    numbers = []
    boards = [[[0 for k in range(5)] for j in range(5)] for i in range(int((len(lines)-1)/6))]
    boardnr = -1
    list = []
    for x in range(len(lines)):
        lines[x] = lines[x].strip()
        if x == 0:
            numbers = lines[x].split(",")
        elif (x-1) % 6 == 0:
            boardnr += 1
        else:
            boards[boardnr][(x-2) % 6] = lines[x].split()
    for number in numbers:
        for b in range(len(boards)):
            if list.count(b) < 1:
                for r in range(5):
                    for c in range(5):
                        if boards[b][r][c] == number:
                            boards[b][r][c] = -1
                if checkwon(boards[b]):
                    x = 0
                    for line in boards[b]:
                        for num in line:
                            if num != -1:
                                x += int(num)
                    print(x*int(number))
                    list.append(b)


method1()
