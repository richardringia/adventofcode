file = open('day 6/tuning_trouble.txt', 'r')
line = file.readline()




def get_first_marker(l):
    first_marker = -1

    i = 0
    while(first_marker == -1):
        j = -1
        x = ''
        for c in line[i:i+l]:
            if c in x:
                break
            elif j == (l-2) and c not in x:
                first_marker = i + j + 2
                break
            x += c
            j += 1
        i += 1
    
    return first_marker

print('awnser 1:', get_first_marker(4))
print('awnser 2:', get_first_marker(14))
