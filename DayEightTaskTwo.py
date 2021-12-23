def unique(comp, display):
    return [disp for disp in display if len(disp) == comp]

def config(display, output):
    display = [''.join(sorted(disp)) for disp in display.split()]
    
    d={i:unique(j, display)[0] for i,j in [(1,2),(4,4),(7,3),(8,7)]}

    d[9] = [disp for disp in display if len(disp)==6 and len(set(disp) - set(d[4])) == 2][0]
    d[3] = [disp for disp in display if len(disp)==5 and len(set(disp) - set(d[7])) == 2][0]
    d[0] = [disp for disp in display if len(disp)==6 and disp not in d[9] and len(set(disp) - set(d[7])) == 3][0]
    d[5] = [disp for disp in display if len(disp)==5 and len(set(disp) - (set(d[4]) - set(d[1]))) == 3][0]
    d[6] = [disp for disp in display if len(disp)==6 and disp not in d.values()][0]
    d[2] = [disp for disp in display if len(disp)==5 and disp not in d.values()][0]

    d_new = dict((v,k) for k,v in d.items())
    return "".join([str(d_new["".join(sorted(out))]) for out in output.split()])

with open('DayEightTaskFile.txt') as test:
    print(sum([int(config(*line.rstrip("\n").split(' | '))) for line in test.readlines()]))