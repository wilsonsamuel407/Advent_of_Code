#AOC2021 count the number of times a depth measurement increases from the previous measurement
# Depth measurments are a list of values in aoc2021_1_input.csv
import pandas as pd
# Data is stored as a csv not a .txt so we don't have strings
mydata = pd.read_csv("aoc2021_1_input.csv", header = None)
# makes a list of lists (1 list for each value in the csv)
df_list = mydata.values.tolist()
# flattens the nested lists
depth_measurments = [val for sublist in df_list for val in sublist]
#now find the difference between n and n+1, if its positive then count n+1
xdiff = [depth_measurments[n]-depth_measurments[n-1] for n in range(0,len(depth_measurments))]
pos_count = 0
for xd in xdiff:
	if xd > 0:
		pos_count +=1
	else:
		pass
print(pos_count)

