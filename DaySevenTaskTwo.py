with open('DaySevenTaskFile.txt') as test:
    l=list(map(int,test.read().split(',')))
    print(min([sum([abs(i - pos)*(abs(i - pos)+1)/2 for i in l]) for pos in range(max(l))]))