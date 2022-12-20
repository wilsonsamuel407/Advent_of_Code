#use pandas to import the data
import pandas as pd
# pandas by default will take a , as the seperator, so need to change that. Also added a header to the csv.
df = pd.read_csv("aoc2021_2_input.csv", sep = " ")
# sumif on 'forward', 'up', 'down'
sum_of_changes = df.groupby('direction')['value'].sum().reset_index(name='obs')
#print(sum_of_changes)
# return sum if as a number (not a dataframe)
up_changes = sum_of_changes.iat[2,1]
down_changes = sum_of_changes.iat[0,1]
forward_changes = sum_of_changes.iat[1,1]
depth_change = down_changes - up_changes
#print(depth_change)
answer = depth_change*forward_changes
print(answer)

