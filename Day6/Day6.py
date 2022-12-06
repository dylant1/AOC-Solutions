from collections import deque
string = ""
f = open("data.txt", "r")
for x in f:
  string += x
buffer = string.split("\n")[0]

q = deque([])
i = 0
while i < len(buffer):
    if len(q) > 13:
        q.popleft()
    q.append(buffer[i])
    if len(set(q)) == len(q) == 14: 
        print(i + 1)
        break
    i += 1


