import collections
def populate(days, d):
    if days > 0: 
        d_new = {i:d[(i+1)%9] if (i+1)%9 in d else 0 for i in range(9)}
        if 0 in d : d_new[6]+=d[0] 
        populate(days - 1, d_new)
    else: print(sum([d[val] for val in d]))

with open('DaySixTaskFile.txt') as test:
        populate(256, dict(collections.Counter(list(map(int,test.read().split(','))))))