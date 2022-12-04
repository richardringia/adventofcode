file = open('day 2/rock_paper_scissors.txt', 'r')
lines = file.readlines()

points = 0
best_points = 0

# Opponent:
#   A = Rock = 0
#   B = Paper = 1
#   C = Scissors = 2
# Player:
#   X = Rock = 0
#   Y = Paper = 1
#   Z = Scissors = 2

# win = 6
# lose = 0
# draw = 3

array_o = ['A', 'B', 'C']
array_y = ['X', 'Y', 'Z']

def calculate(o, y):
    point = 0

    if o == y:
        point += 3
    else:
        if (y == 0 and o == 2) or (y == 1 and o == 0) or (y == 2 and o == 1):
            point += 6
    point += (y + 1)

    return point

def calculate2(o, y):
    if y == 0:
        if o == 0:
            y = 2
        elif o == 1: 
            y = 0
        else:
            y = 1
    elif y == 2:
        if o == 0:
            y = 1
        elif o == 1:
            y = 2
        else:
            y = 0
    else:
        y = o

    return calculate(o, y)



for line in lines:
    o = array_o.index(line[0])
    y = array_y.index(line[2])

    points += calculate(o, y)
    best_points += calculate2(o, y)


print('awnser 1:', points)
print('awnser 2:', best_points)