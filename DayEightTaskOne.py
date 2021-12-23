def unique(display, output):
    return sum([sum([1 for out in output.split() if sorted(out) == sorted(disp) and len(out) in[2,3,4,7]]) for disp in display.split()])
with open('DayEightTaskFile.txt') as test:
    print(sum([unique(*line.rstrip("\n").split(' | ')) for line in test.readlines()]))