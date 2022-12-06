string = ""
f = open("data.txt", "r")
for x in f:
  string += x

tmp = string.split("\n")
blocks = []
instructions = []
for i, val in enumerate(tmp):
    tmp2 = val
    if not tmp2:
        instructions = [tmp[i+1:-1]]
        break
    if tmp2[0] == "[" or tmp2[0] == " ":
        blocks.append(tmp2)
stacks = []
for i in range(0, len(blocks) - 1):
    levels = blocks[i].split(" ")
    print(levels)
    newlevel = []
    j = 0
    while j < len(levels):
        if not levels[j]:
            newlevel.append(" ");
            j += 4
        else:
            newlevel.append(levels[j])
            j += 1
    stacks.append(newlevel)
levels = [[] for _ in range(len(stacks[0]))]
for i in range(len(stacks)):
    for j in range(len(stacks[i])):
        levels[j].append(stacks[i][j])
for i in range(len(levels)):
    levels[i] = levels[i][::-1]
    if len(levels[i]) <= 0 or not levels[i][-1]:
        continue

    while len(levels[i]) > 0 and levels[i][-1] == " ":
        levels[i].pop()
for instruction in instructions[0]:
    vals = instruction.split(" ")
    nmoved = int(vals[1])
    fromindex = int(vals[3]) - 1
    toindex = int(vals[5]) - 1
    popped = []
    for i in range(nmoved):
        try:
            tmpval = levels[fromindex].pop()
            #levels[toindex].append(tmpval)
            popped.append(tmpval)
        except:
            break
    for j in range(len(popped) - 1, -1, -1):
        levels[toindex].append(popped[j])
res = ""
for col in levels:
    if not len(col) > 0:
        continue
    if col[-1]:
        end = col[-1].strip("[").strip("]")
        res += end
print(res)


