readings = []
with open('DayFourTaskFile.txt') as test:
    readings = [list(line.strip('\n')) for line in test.readlines()]

numbers = list(map(int,numbers.split(',')))
boards = [[[int(spl) for spl in split.split()] for split in board.split('\n')] for board in boards]

def readBoard(board, numbers):
    smallRow = min([max([numbers.index(num) for num in line]) for line in board+[[line[i] for line in board] for i in range(len(board[0]))]])
    return (smallRow, sum([sum([num for num in line if numbers.index(num)>smallRow]) for line in board]))

d=dict([readBoard(board, numbers) for board in boards])
print(numbers[max(d)]*d[max(d)])