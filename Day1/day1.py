def getMax(s):
    elves = s.split("\n\n")

    tmp: list[int] = []
    for elf in elves:
        t = elf.split("\n")
        s = 0
        for val in t:
            if val:
                s += int(val)
        tmp.append(s)

    res = []

    for _ in range(3):
        res.append(max(tmp))
        tmp.pop(tmp.index(max(tmp)))

    return sum(res)

string = ""
f = open("data.txt", "r")
for x in f:
    string += x

print(getMax(string))


