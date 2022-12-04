file = open('day 4/camp_cleanup.txt', 'r')
lines = file.readlines()

count1 = 0
count2 = 0

for group in lines:
    prevStart = None
    prevEnd = None
    for assigments in group.split(','):
        worker = ""
        start, end = assigments.split('-')
        start = int(start)
        end = int(end)
        
        if prevStart == None and prevEnd == None:
            prevStart = start
            prevEnd = end
        else:
            if (start <= prevStart and end >= prevEnd) or (prevStart <= start and prevEnd >= end):
                count1 += 1

            if start <= prevStart <= end or start <= prevEnd <= end or prevStart <= start <= prevEnd or prevStart <= end <= prevEnd:
                count2 += 1

print(count1)
print(count2)