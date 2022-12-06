string = ""
f = open("data.txt", "r")
for x in f:
  string += x

score = 0

arr = string.split("\n")

m2 = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
for game in arr:
    if len(game) > 2:
        if game[0] == "A":
            if game[2] == "X":
                score += 0
                score += 3
            elif game[2] == "Y":
                score += 3
                score += 1
            else:
                score += 6 
                score += 2
            
        elif game[0] == "B":
            if game[2] == "X":
                score += 0
                score += 1
            elif game[2] == "Y":
                score += 3
                score += 2
            else:
                score += 6
                score += 3
        else:
            if game[2] == "X":
                score += 0
                score += 2 
            elif game[2] == "Y":
                score += 3
                score += 3 
            else:
                score += 6
                score += 1


print(score)



