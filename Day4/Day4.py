m = []

while True:
    try:
        nput = input()
        m.append(nput)
    except:
        break

res = 0
for assignment in m:
    tmp = assignment.split(",")
    times = [time.split("-") for time in tmp]
    if not assignment:
        continue
    if int(times[0][0]) <= int(times[1][0]) and int(times[0][1]) >= int(times[1][1]):
        res += 1
    elif int(times[0][0]) >= int(times[1][0]) and int(times[0][1]) <= int(times[1][1]):
        res += 1

    elif int(times[0][0]) <= int(times[1][1]) and int(times[1][0]) <= int(times[0][1]):
        res += 1
    elif int(times[0][0]) >= int(times[1][1]) and int(times[1][0]) >= int(times[0][1]):
        res += 1


print(res)
