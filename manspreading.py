from random import choice, randint

#counts empty seats in a car
#seats defined as two half-seats, so next half-seat over must be empty ('E') too
def countseats(car):
	count = 0
	for j in range(0, len(car)):
		for i in range(0,len(car[j]),2):
			if car[j][i] == 'E' and car[j][i+1] == 'E':
				count=count+1
	return count


#simulates normal passenger randomly choosing available seat, i.e. replacing two 'E's
def normsit(lyst):
	available = []

	for j in range(0, len(lyst)):
		for i in range(0,len(lyst[j]),2):
			if lyst[j][i] == 'E' and lyst[j][i+1] == 'E':
				available.append([j,i])

	if len(available) !=0:
		sit = choice(available)
		lyst[sit[0]][sit[1]] = 'N'
		lyst[sit[0]][sit[1]+1] = 'N'

	else:
		pass


#simulates manspreader randomly choosing available seat, i.e. replacing four 'E's
def spreadsit(lyst):
	available = []

	for j in range(0, len(lyst)):
		for i in range(2,len(lyst[j])-2,2):
			if lyst[j][i] == 'E' and lyst[j][i+1] == 'E' \
			and lyst[j][i+2] == 'E' and lyst[j][i-1] == 'E':
				available.append([j,i])
	
	if len(available) != 0:
		sit = choice(available)
		lyst[sit[0]][sit[1]] = 'S'
		lyst[sit[0]][sit[1]+1] = 'S'
		lyst[sit[0]][sit[1]-1] = 'S'
		lyst[sit[0]][sit[1]+2] = 'S'
	
#counts number of normal sitters
def normcount(lyst):
	total = 0
	for j in lyst:
		for i in j:
			if i == 'N':
				total = total +1
	return total/2

#counts number of manspreading sitters
def spreadcount(lyst):
	total = 0
	for j in lyst:
		for i in j:
			if i == 'S':
				total = total +1
	return total/4


#assigns max normal sitters (women) given number of manspreaders
#based on synchronous reorginzation; consult seating chart for explanation

max ={1:41, 2: 39, 3: 37, 4:34, 5:32, 6:30, 7:27,
	8:25, 9:23, 10:20, 11:18, 12:16, 13:13, 14:10}

#ten thousand simulations
for i in range(10000):

#sets empty car
	eight1 = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
	eight2 = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
	eight3 = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
	eight4 = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']

	four1 = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
	four2 = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']

	two1 = ['E', 'E', 'E', 'E']
	two2 = ['E', 'E', 'E', 'E']

	car =[eight1, eight2, eight3, eight4, four1, four2, two1, two2]

#feeds passengers into car until full; option to print seating chart 
	while countseats(car)>0:
		x = randint(0,1)
				
		if x == 0:
			normsit(car)
			#for i in car:
				#print i
		else:
			spreadsit(car)
			#for i in car:
				#print i

	women = normcount(car)
	men = spreadcount(car)
	maxwomen = max[men]
	total = men + women
	adjtotal = men + maxwomen

	print men, women, maxwomen, total, adjtotal












