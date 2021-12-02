readings = []
with open('DayTwoTaskFile.txt') as test:
    readings = [line.split() for line in test.readlines()]

horizontal = 0
depth = 0
aim = 0
for i in range(len(readings)):
    if(readings[i][0] == 'forward'):
        horizontal += int(readings[i][1])
        depth += aim * int(readings[i][1])
    if(readings[i][0] == 'up'):
        aim -= int(readings[i][1])
    if(readings[i][0] == 'down'):
        aim += int(readings[i][1])

result = horizontal*depth

print(result)