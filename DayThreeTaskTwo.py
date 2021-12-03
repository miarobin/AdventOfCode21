import re

readings = []
with open('DayThreeTaskFile.txt') as test:
    readings = [line.strip('\n') for line in test.readlines()]

def criteria(temp, column, thing):
    return list(filter(lambda a: re.search(rf'.{{{column}}}{thing}.{{{(len(temp[0])-column-1)}}}',a)!=None,temp))
    #return [a for a in temp if re.search(rf'.{{{column}}}{thing}.{{{(len(temp[0])-column-1)}}}',a)!=None]

def oFinder(temp, column):
    if len(temp) == 1:
        return temp[0]

    temp = criteria(temp, column, 1 if(sum([int(line[column]) for line in temp])>=len(temp)/2) else 0)

    return oFinder(temp,column+1)


def co2Finder(temp, column):
    if len(temp) == 1:
        return temp[0]

    temp = criteria(temp, column, 1 if(sum([int(line[column]) for line in temp])<len(temp)/2) else 0)

    return co2Finder(temp,column+1)


print(int(oFinder(readings,0),2)*int(co2Finder(readings,0),2))
