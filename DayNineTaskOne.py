def lowPoint(array):
    grid = [[10 for i in range(len(array[0])+2)]] + [[10] + line + [10] for line in array] + [[10 for i in range(len(array[0])+2)]]
    return sum([grid[i][j]+1 for i in range(1,len(grid)-1) for j in range(1,len(grid[0])-1) if grid[i][j]<grid[i+1][j] and grid[i][j]<grid[i][j+1] and grid[i][j]<grid[i][j+1] and grid[i][j]<grid[i-1][j] and grid[i][j]<grid[i][j-1]])

with open('DayNineTaskFile.txt') as test:
    print(lowPoint([list(map(int, line.strip("\n"))) for line in test.readlines()]))