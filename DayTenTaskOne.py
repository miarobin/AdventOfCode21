def closed():
    all([[ if br in for br, j in enumerate(brackets:-)] if brack in ('(','[','{','<') for brack, i in enumerate(brackets)])


with open('DayNineTaskFile.txt') as test:
    print(closed([list(map(int, line.strip("\n"))) for line in test.readlines()]))