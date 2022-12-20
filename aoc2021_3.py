# load the data
with open("aoc2021_3_input.txt", "r") as flattened1:
	flattened2 = flattened1.readlines()
#its a list of strings here with /n included, strip /n out
binary = []
for f in flattened2:
	g = f.strip()
	binary.append(g)

lists = []
intlists = []
digit1 = 0
digit2 = 0
digit3 = 0
digit4 = 0
digit5 = 0
digit6 = 0
digit7 = 0
digit8 = 0
digit9 = 0
digit10 = 0
digit11 = 0
digit12 = 0


#now to make one massive list of bits, 1 list entry per bit
for b in binary:
	for char in b:
		lists.append(char)
for l in lists:
	intl = int(l,2) 
	intlists.append(intl)

# i know that the first bit will be the 1st, 13th, 26th entry of that list. 
for r in range(0,len(intlists),12):
	digit1 += intlists[r]
for r in range(1,len(intlists),12):
	digit2 += intlists[r]
for r in range(2,len(intlists),12):
	digit3 += intlists[r]
for r in range(3,len(intlists),12):
	digit4 += intlists[r]
for r in range(4,len(intlists),12):
	digit5 += intlists[r]
for r in range(5,len(intlists),12):
	digit6 += intlists[r]
for r in range(6,len(intlists),12):
	digit7 += intlists[r]
for r in range(7,len(intlists),12):
	digit8 += intlists[r]
for r in range(8,len(intlists),12):
	digit9 += intlists[r]
for r in range(9,len(intlists),12):
	digit10 += intlists[r]
for r in range(10,len(intlists),12):
	digit11 += intlists[r]
for r in range(11,len(intlists),12):
	digit12 += intlists[r]


list_of_digits = [digit1,digit2 ,digit3, digit4, digit5, digit6, digit7, digit8, digit9, digit10, digit11, digit12]
#print(list_of_digits)

# now i have the total number of 1's i can dtermine if they are more than half of all entries to find the most common bit
gamma = []
epsilon = []
divideby = len(intlists)/12
for li in list_of_digits:
	if li/divideby >=0.5:
		gamma.append("1")
	else:
		gamma.append("0")
epsilon = []
for g in gamma:
	if g == "1":
		epsilon.append("0")
	else:
		epsilon.append("1")
# didn't think yet how to automatically ger the results there back into a binary string so manually added.
#gamma = "100111100011"
#epsilon = "011000011100"
#print(gamma)
#print(epsilon)
s =  ''.join(gamma)
y = ''.join(epsilon)
print(s)
print(y)


gammaint = int(s,2)
epsilonint = int(y,2)
print(gammaint)
print(epsilonint)
answer = gammaint*epsilonint
print(answer)	
