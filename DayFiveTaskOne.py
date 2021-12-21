import collections
readings = []
with open('DayFiveTaskFile.txt') as test:
    readings = [list(map(int, line.strip('\n').replace(' -> ', ',').split(','))) for line in test.readlines()]
l=dict(collections.Counter([(x,y) for xi,yi,xf,yf in readings for y in range(min(yi,yf),max(yi,yf)+1) for x in range(min(xi,xf),max(xi,xf)+1) if xi==xf or yi==yf]))
print(sum([1 for count in l.values() if count>=2]))