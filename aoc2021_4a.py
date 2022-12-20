# turn everything into one large list, removing the whitespace that helps distinguish between boards. 
# each list entry will be one row.
# where there is an /n between boards this is shown a blank list entry
import numpy as np
with open('aoc2021_4_input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
#print(lines)

# to extract the random numbers make a new list and append the first entry of 'lines' to it, then seperate it componant parts, finally convert those componant parts to integers.
nums = [int(n) for n in lines.pop(0).split(',')]
#print(nums)

# to extract the boards.
boards = []
board = []
#only from the second entry since the first entry is used for the above random numbers.
for line in lines[1:]:
#if not is used to conditionally execture a block if the value is empty or false
    if not line:
        boards.append(board)
        board = []
    else:
        board.append([int(n) for n in line.strip().split()])

# we need another one here since lines doesn't end with a '' so the last board wont get added.          
boards.append(board)
#print(boards)
#print(len(boards))
# part 1
counts = np.zeros(shape=(len(boards), 5, 5))
#print(counts)

for num in nums:
	# in the first board
    for i, board in enumerate(boards):
    #in the first row
        for y, row in enumerate(board):
            if num in row:
                #if its in there then return its position
                x = row.index(num)
                counts[i][y][x] = 1

    for j, count in enumerate(counts):
        if any(n for n in count.sum(axis=0) == 5) or any(j for j in count.sum(axis=1) == 5):
            break

    else:
    	continue

    break

part1 = int(np.sum((1 - count) * boards[j]) * num)
#print(f'part 1: {part1}')

# part 2
# counts is a list of boards made up of zeros ready to be marked if a match
counts = np.zeros(shape=(len(boards),5,5))
# index winners will be a list of the boards that have a completed row. Boards are given a position 1, 2, 3 etc according their order in the list boards.
index_winners = []
winning_counts =[]
#num is the random numbers to match
for num in nums:
    for i, board in enumerate(boards):
         for y, row in enumerate(board):
            if num in row and i not in index_winners:
                x = row.index(num)
                counts[i][y][x] = 1
    
    for i, count in enumerate(counts):
        print(count)
        if i not in index_winners and (any(n for n in count.sum(axis=0) == 5) or any(j for j in count.sum(axis=1) == 5)):
            index_winners.append(i)
            winning_counts.append((i, num, np.array(count)))

#print(index_winners)
idx, num, count = winning_counts[-1]
#print(winning_counts[-1])
#part2 = int(np.sum((1 - count) * boards[idx]) * num)
#print(f'part 1: {part2}')