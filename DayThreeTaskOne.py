readings = []
with open('DayThreeTaskFile.txt') as test:
    readings = [list(line.strip('\n')) for line in test.readlines()]

result = [sum([int(line[i]) for line in readings]) for i in range(len(readings[0]))]

gamma = int(''.join(['1' if res>len(readings)/2 else '0' for res in result]),2)
epsilon = int(''.join(['1' if res<len(readings)/2 else '0' for res in result]),2)

print(gamma*epsilon)
