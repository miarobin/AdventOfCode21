import re

readings = []
with open('DayThreeTaskFile.txt') as test:
    readings = [line.strip('\n') for line in test.readlines()]


def oFinder(temp, column):
    if len(temp) == 1:
        return temp[0]

    if(sum([int(line[column]) for line in temp])>=len(temp)/2):
        temp = list(filter(lambda a: re.search(rf'.{{{column}}}1.{{{(len(temp[0])-column-1)}}}',a)!=None,temp))

    else:
        temp = list(filter(lambda a: re.search(rf'.{{{column}}}0.{{{(len(temp[0])-column-1)}}}',a)!=None,temp))

    return oFinder(temp,column+1)


def co2Finder(temp, column):
    if len(temp) == 1:
        return temp[0]

    if(sum([int(line[column]) for line in temp])<len(temp)/2):
        temp = list(filter(lambda a: re.search(rf'.{{{column}}}1.{{{(len(temp[0])-column-1)}}}',a)!=None,temp))

    else:
        temp = list(filter(lambda a: re.search(rf'.{{{column}}}0.{{{(len(temp[0])-column-1)}}}',a)!=None,temp))

    return co2Finder(temp,column+1)


print(int(oFinder(readings,0),2)*int(co2Finder(readings,0),2))
