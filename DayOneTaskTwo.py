readings = []
with open('DayOneTaskFile.txt') as test:
    readings = [int(line) for line in test.readlines()]

largerThanPrev = sum([1 if readings[i+3]>readings[i] else 0 for i in range(len(readings)-3)])
print(largerThanPrev)