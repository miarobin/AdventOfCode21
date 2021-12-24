from functools import reduce
def collBasin(array):
    grid = [[10 for i in range(len(array[0])+2)]] + [[10] + line + [10] for line in array] + [[10 for i in range(len(array[0])+2)]]
    basins = [len(basin(grid, set(), i, j))  for i in range(1,len(grid)-1) for j in range(1,len(grid[0])-1) if grid[i][j]<grid[i+1][j] and grid[i][j]<grid[i][j+1] and grid[i][j]<grid[i][j+1] and grid[i][j]<grid[i-1][j] and grid[i][j]<grid[i][j-1]]
    
    return reduce(lambda x, y: x*y, sorted(basins)[-3:])

def basin(grid, b, i, j):
    b.add((i,j))
    for n in [-1,+1]:
        if grid[i+n][j]<9 and not (i+n,j) in b:
            b.union(basin(grid, b, i+n, j))

    for n in [-1,+1]:
        if grid[i][j+n]<9 and not (i,j+n) in b:
            b.union(basin(grid, b, i, j+n))
    return b


with open('DayNineTaskFile.txt') as test:
    print(collBasin([list(map(int, line.strip("\n"))) for line in test.readlines()]))