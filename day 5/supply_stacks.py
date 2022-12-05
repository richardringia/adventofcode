file = open('day 5/supply_stacks.txt', 'r')
lines = file.readlines()

moves = []
stacks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7:[], 8: []}


for line in lines:
    if "move" in line:
       line = line.replace('move ', '').replace('from ', '').replace('to ', '').replace('\n', '')
       moves.append(line.split(' '))


    else:
        i = 0
        j = 0
        for c in line:
            if i % 4 == 1:
                if c != " " and c.isalpha():
                    stacks.get(j).insert(0, c)
                j += 1  
            i += 1

for move in moves:
    c = int(move[0])
    crates = stacks.get(int(move[1]) - 1)
    mc = crates[-c:]
    del crates[-c:]

    # part one: for _c in mc[::-1]:
    for _c in mc:
        stacks.get(int(move[2]) - 1).append(_c)
    pass

result = ""
for stack in stacks:
    result += stacks[stack][-1]

print(result)