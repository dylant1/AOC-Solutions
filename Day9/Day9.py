string = ""
f = open("data.txt", "r")
for x in f:
  string += x
aInput = string.split("\n")[:-1]
#print(aInput)


i = 0

head = [0, 0]
tail = [0, 0]
visited = []

def updateHead(x, y):
    head[0] += x
    head[1] += y
    #check tail
    headX, tailX = head[0], tail[0]
    headY, tailY = head[1], tail[1]

    if headX == tailX:
        difference = headY - tailY
        if abs(difference) > 1:
            if difference > 0:
                tail[1] += 1
            elif difference < 0:
                tail[1] -= 1
    elif headY == tailY:
        difference = headX - tailX
        if abs(difference) > 1:
            if difference > 0:
                tail[0] += 1
            elif difference < 0:
                tail[0] -= 1
    else:
        differenceX = headX - tailX
        differenceY = headY - tailY
        if abs(differenceX) > 1:
            #four quadrants

            if differenceX > 0 and differenceY > 0:
                tail[0] += 1
                tail[1] += 1
            elif differenceX > 0 and differenceY < 0:
                tail[0] += 1
                tail[1] -= 1
            elif differenceX < 0 and differenceY > 0:
                tail[0] -= 1
                tail[1] += 1
            elif differenceX < 0 and differenceY < 0:
                tail[0] -= 1
                tail[1] -= 1
        elif abs(differenceY) > 1:
            if differenceX > 0 and differenceY > 0:
                tail[0] += 1
                tail[1] += 1
            elif differenceX > 0 and differenceY < 0:
                tail[0] += 1
                tail[1] -= 1
            elif differenceX < 0 and differenceY > 0:
                tail[0] -= 1
                tail[1] += 1
            elif differenceX < 0 and differenceY < 0:
                tail[0] -= 1
                tail[1] -= 1
    #print(tail)
    visited.append(tail[:])


while i < len(aInput):
    direction = aInput[i][0]
    amt = int(aInput[i][2])

    if direction == "U":
        for _ in range(amt):
            updateHead(0, 1)
    elif direction == "D":
        for _ in range(amt):
            updateHead(0, -1)
    elif direction == "L":
        for _ in range(amt):
            updateHead(-1, 0)
    elif direction == "R":
        for _ in range(amt):
            updateHead(1, 0)






    i += 1

#print(visited)
print(visited)
res = []
for tile in visited:
    if tile in res:
        continue
    res.append(tile)

print(len(res))
