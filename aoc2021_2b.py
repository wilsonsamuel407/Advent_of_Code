import pandas as pd
data = pd.read_csv("aoc2021_2_input.csv", delimiter = " ")
df_list = data.values.tolist()
Direction = [val for sublist in df_list for val in sublist]
#Direction = ['forward', 5, 'down', 9, 'forward', 2, "up", 2, "forward", 4]
aim = 0
position = 0
depth = 0
for r in range(0,1999):
	target = Direction[r]
	tbs = Direction[r+1]
	if target == "forward":
		position += tbs
		depth += tbs*aim
	elif target == "up":
		aim -= tbs
	elif target == "down":
		aim += tbs
	else:
		pass
print(position, depth)
answer = position*depth
print(answer)
