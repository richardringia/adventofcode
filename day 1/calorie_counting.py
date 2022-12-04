file = open('day 1/calories.txt', 'r')
lines = file.readlines()

count = 0

elves = []

for line in lines:
    if line == '\n':
        count += 1
    else:
        if len(elves) - 1 < count:
            elves.append(int(line))
        else:
            elves[count] = elves[count] + int(line)

most_elve = 0


for elve in elves:
    if elve > most_elve:
        most_elve = elve

print('awnser 1:', most_elve)



top_three_elves = [0] * 3


for i in range(len(top_three_elves)):
    h = 0
    for elve in elves:
        if elve > h:
            h = elve
    
    elves.remove(h)
    top_three_elves[i] = h
        

print('awnser 2:', sum(top_three_elves))