def insert(poly, count):
    insertions = []
    for x in count:
        c = count[x]
        insertions.append((poly[x][0], c))
        insertions.append((poly[x][1], c))
        count[x] = 0
    for i in insertions:
        count[i[0]] += i[1]
    return count


def method():
    file1 = open("input files/day14.txt")
    lines = file1.readlines()
    string = lines[0].strip()
    poly = {}
    count = {}
    for x in range(2, len(lines)):
        split = lines[x].strip().split(" -> ")
        poly[split[0]] = (split[0][0]+split[1], split[1]+split[0][1])
        count[split[0]] = 0
    for x in range(len(string)-1):
        count[string[x:x+2]] += 1
    for x in range(40):
        count = insert(poly, count)
    c = {}
    for x in count:
        for y in range(2):
            if x[y] in c:
                c[x[y]] += count[x]
            else:
                c[x[y]] = count[x]
    print(int(max(c.values())/2-min(c.values())/2+0.5))


method()
