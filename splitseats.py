from random import choice

#need split countseats functions now
def countseats_W(car):
	count = 0
	for j in range(0, len(car)):
		for i in range(0,len(car[j]),2):
			if car[j][i] == 'E' and car[j][i+1] == 'E':
				count=count+1
	return count

def countseats_M(lyst):
	count = 0
	for j in range(0, len(lyst)):
		for i in range(2,len(lyst[j])-2,2):
			if lyst[j][i] == 'E' and lyst[j][i+1] == 'E' \
			and lyst[j][i+2] == 'E' and lyst[j][i-1] == 'E':
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
	
	else:
		pass


	
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


#five thousand female simulations
for i in range(5000):

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

	Mcar = [eight1, eight2, eight3, eight4, four1, four2, two1, two2]
	Wcar = [eight1, eight2, eight3, eight4, four1, four2, two1, two2]

#feeds passengers into car until full; option to print seating chart 
	while countseats_W(Wcar)>0:
		normsit(Wcar)
		#for i in car:
			#print i

	women = normcount(Wcar)	

	print women

#five thousand male simulations
for i in range(5000):

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

	Mcar = [eight1, eight2, eight3, eight4, four1, four2, two1, two2]

	
#feeds passengers into car until full; option to print seating chart 
	while countseats_M(Mcar) > 0:
		spreadsit(Mcar)
		#for i in car:
			#print i

	men = spreadcount(Mcar)	

	print men








