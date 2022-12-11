file = open('day 10/cathode_ray_tube.txt', 'r')
lines = file.readlines()


x = 1
y = 0
z = 0
c = 0
for line in lines:
    line = line.replace('\n', '')
    n = line == "noop"

    for i in range(1, 2 if n else 3): 
            # if (c + i) % (20 + 40 * z) is 0:
            if (c + i) in [20, 60, 100, 140, 180, 220]:
                y += (c + i) * x
                z += 1

    if n:
        c += 1
    else:            
        x += int(line.replace('addx ', ''))
        c += 2



print('awnser 1:', y)
