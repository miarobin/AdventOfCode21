import collections
readings = []
with open('DayFiveTaskFile.txt') as test:
    readings = [list(map(int, line.strip('\n').replace(' -> ', ',').split(','))) for line in test.readlines()]
sign = lambda x: 1 if x>=0 else -1
l=dict(collections.Counter([(x,y) for xi,yi,xf,yf in readings for y in range(min(yi,yf),max(yi,yf)+1) for x in range(min(xi,xf),max(xi,xf)+1) if xi==xf or yi==yf] 
                            + [(xi+i*sign(xf-xi),yi+i*sign(yf-yi)) for xi,yi,xf,yf in readings for i in range(abs(xf-xi)+1) if abs(xf-xi)==abs(yf-yi)]))
print(sum([1 for count in l.values() if count>=2]))