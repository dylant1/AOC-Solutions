from collections import defaultdict
string = ""
f = open("data.txt", "r")
for x in f:
  string += x

#print(string)

files = []
mem = defaultdict(lambda : 0)
for cmd in string.split("\n"):
    cmd = cmd.split(" ")
    #print(cmd#)
    currDir = "/"
    if len(files) > 0: currDir = files[-1] if files[-1] != '' else "/"
    if cmd[0] == "$":
        if cmd[1] == "cd" and cmd[2] == "/":
            files.append("")
        elif cmd[1] == "cd" and cmd[2] == "..":
            files.pop()
        elif cmd[1] == "cd":
            files.append("".join(files) + "/" + cmd[2])
    else:
        #print(" ")
        if cmd[0].isnumeric():
            #mem[currDir] += int(cmd[0])
            for i in range(len(files)):
                if files[i] == "":
                    mem["/"] += int(cmd[0])
                else:
                    mem[files[i]] += int(cmd[0])

left = 70000000 - mem["/"]
res = 0
tmp2 = []
for v in mem.values():
    #print(v)
    #if v <= 100000:
        #res += v
    if v + left >= 30000000: tmp2.append(v)

print(min(tmp2))


    

#print(mem)
#print(res)


    

