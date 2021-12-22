with open('DaySevenTaskFile.txt') as test:
    l=list(map(int,test.read().split(',')))
    print(min([sum([abs(i - pos) for i in l]) for pos in range(max(l))]))