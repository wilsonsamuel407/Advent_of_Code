# load the data
#with open("aoc2021_3_input.txt", "r") as flattened1:
	#flattened2 = flattened1.readlines()
#its a list of strings here with /n included, strip /n out
#binary = []
#for f in flattened2:
	#g = f.strip()
	#binary.append(g)
binary = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

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
#print(intlists)

# i know that the first bit will be the 1st, 13th, 26th entry of that list. 
iter1 = []
newrange0 = len(intlists)
#add up the number of 1's as a first step to determining if they are the most common bit
for r in range(0,newrange0,5):
	digit1 += intlists[r]
# now divide by number of bits per entry to determine number of entries and half to see if most common.
if digit1 >= newrange0/10:
# now recover all those entries where the first digit is 1
	for r in range(0,len(intlists),5):
		#print(r)
		if intlists[r] == 1:
			for t in range(r,r+5):
				iter1.append(intlists[t])
else:
	pass

#print(newrange0)
#print(digit1)
#print(iter1)

iter2 = []
newrange1 = len(iter1)
#print(newrange1)
for r in range(1,newrange1,5):
	digit2 += iter1[r]
if digit2 >= newrange1/10:
	for r in range(0,newrange1,5):
		if iter1[r+1] == 1:
			for t in range(r,r+5):
				iter2.append(iter1[t])
else:
	for r in range(0,newrange1,5):
		if iter1[r+1] == 0:
			for t in range(r,r+5):
				iter2.append(iter1[t])

#print(digit2)
#print(iter2)

iter3 = []
newrange2 = len(iter2)
#print(newrange2)
for r in range(2,newrange2,5):
	digit3 += iter2[r]
if digit3 >= newrange2/10:
	for r in range(0,newrange2,5):
		if iter2[r+2] == 1:
			for t in range(r,r+5):
				iter3.append(iter2[t])
else:
	for r in range(0,newrange2,5):
		if iter2[r+2] == 0:
			for t in range(r,r+5):
				iter3.append(iter2[t])

#print(digit3)
#print(iter3)

iter4 = []
newrange3 = len(iter3)
#print(newrange3)
for r in range(3,newrange3,5):
	digit4 += iter3[r]
if digit4 >= newrange3/10:
	for r in range(0,newrange3,5):
		if iter3[r+3] == 1:
			for t in range(r,r+5):
				iter4.append(iter3[t])
else:
	for r in range(0,newrange3,5):
		if iter3[r+3] == 0:
			for t in range(r,r+5):
				iter4.append(iter3[t])

#print(digit3)
#print(iter4)

iter5 = []
newrange4 = len(iter4)
#print(newrange4)
for r in range(4,newrange4,5):
	digit5 += iter4[r]
if digit5 >= newrange4/10:
	for r in range(0,newrange4,5):
		if iter4[r+4] == 1:
			for t in range(r,r+5):
				iter5.append(iter4[t])
else:
	for r in range(0,newrange4,5):
		if iter4[r+4] == 0:
			for t in range(r,r+5):
				iter5.append(iter4[t])

#print(digit3)
#print(iter5)

listofiters = [iter1,iter2,iter3,iter4,iter5]
for listof in listofiters:
	if len(listof) == 5:
		s = [str(x) for x in listof]
		y =  ''.join(s)
		oxygengenerator = int(y,2)
		print(oxygengenerator)
	else:
		pass