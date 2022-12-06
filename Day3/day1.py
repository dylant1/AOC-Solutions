def day3(s):
    t = s.split("\n")
    res = 0
    res2 = 0

    for val in t:
        firsthalf, secondhalf = val[:len(val)//2], val[len(val)//2:]
        same = ''.join(set(firsthalf).intersection(secondhalf))

        for char in same:
            if char.isupper():
                res += ord(char) - ord('A') + 26 + 1
            else:
                res += ord(char) - ord('a') + 1

    sublist = [t[n:n+3] for n in range(0, len(t), 3)]
    for group in sublist:
        if len(group) == 1:
            continue
        same1 = ''.join(set(group[0]).intersection(group[1]))
        same2 = ''.join(set(same1).intersection(group[2]))
        #print(same2)
        
        for char in same2:
            print(char)
            if char.isupper():
                res2 += ord(char) - ord("A") + 27
                print(ord(char) - ord('A') + 27)
            else:
                res2 += ord(char) - ord('a') + 1
                print(ord(char) - ord('a') + 1)


    return res2


string = ""
f = open("data.txt", "r")
for x in f:
    string += x


print(day3(string))

