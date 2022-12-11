string = ""
f = open("data.txt", "r")
for x in f:
  string += x
aInput = string.split("\n")[:-1]
#
tmp2 = aInput[0]
res = 0
for tmp in range(len(aInput[0])):
    if aInput[0][tmp] == "(":
        res += 1
    elif aInput[0][tmp] == ")":
        res -= 1
    if res < 0:
        print(tmp)
        break
#print(res)
