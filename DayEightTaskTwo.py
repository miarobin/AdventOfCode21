def checknum(length, check, display, d):
    return next(disp for disp in display if len(disp) == length and check(disp, d))

def config(display, output):
    display = [''.join(sorted(disp)) for disp in display.split()]
    
    d={i:checknum(j, lambda x, di :True, display, {}) for i,j in [(1,2),(4,4),(7,3),(8,7)]}
    d={**d,**{i:checknum(n, f, display, d) for i, n, f in [(9, 6, lambda x, di: len(set(x) - set(di[4])) == 2),
                                                    (3, 5, lambda x, di: len(set(x) - set(di[7])) == 2),
                                                    (0, 6, lambda x, di: len(set(x) - set(di[7])) == 3 and x not in di.values()),
                                                    #(0, 6, lambda x, di: len(set(x) - set(di[7])) == 3 and not len(set(x) - set(di[4])) == 2),
                                                    (5, 5, lambda x, di: len(set(x) - (set(di[4]) - set(di[1]))) == 3)]}}
    d={**d,**{i:checknum(n, lambda x, di: x not in di.values(), display, d) for i, n in [(6, 6), (2, 5)]}}

    d_new = {v:k for k,v in d.items()}
    return "".join([str(d_new["".join(sorted(out))]) for out in output.split()])

with open('DayEightTaskFile.txt') as test:
    print(sum([int(config(*line.rstrip("\n").split(' | '))) for line in test.readlines()]))