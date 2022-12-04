file = open('day 3/rucksack_reorganization.txt', 'r')
lines = file.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0
sum2 = 0

for line in lines:
    middle = len(line) // 2
    str1, str2 = line[:middle], line[middle:]
    
    double = None

    for s1 in str1:
        for s2 in str2:
            if s1 == s2:
                double = s1

    sum += alphabet.index(double) + 1
    
for group in range(len(lines) // 3):
    badge = None
    for line1 in lines[group * 3]:
        for line2 in lines[group * 3+ 1]:
            for line3 in lines[group * 3 + 2]:
                if line1 == line2 == line3 and line1 != "\n" and line2 != "\n" and line3 != "\n":
                    badge = line1

    sum2 += alphabet.index(badge) + 1


print(sum)
print(sum2)
    
    