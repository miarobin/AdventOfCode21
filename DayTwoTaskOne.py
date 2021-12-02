readings = []
with open('DayTwoTestFile.txt') as test:
    readings = [line.split() for line in test.readlines()]

horizontal = 0
depth = 0
for i in range(len(readings)):
    if(readings[i][0] == 'forward'):
        horizontal += int(readings[i][1])
    if(readings[i][0] == 'up'):
        depth -= int(readings[i][1])
    if(readings[i][0] == 'down'):
        depth += int(readings[i][1])

result = horizontal*depth

print(result)
