import csv
import numpy
import random

city = numpy.zeros((100, 100))
sites = {}

z = 0 
with open('top-1m.csv', 'r') as csvfile:
     handle = csv.reader(csvfile)
     i = 0
     j = 0
     while z < 50:
 		lines = []
	 	dim = i+j+1
	 	if dim == 1:
	 		num = 1
	 		lines.append(tuple(handle.next()))
	 		tuply = lines.pop()
	 		city[49][49] = 100-(int(tuply[0])/100)
	 		sites[(49,49)] = tuply[1]
	 	else:
 			num = dim*4-4

	 		for x in xrange(num):
	 			lines.append(tuple(handle.next()))

	 		for I in xrange(dim):
	 			tuply = random.choice(lines)
				city[49-i+I][49-j] = 100-(int(tuply[0])/100)
				sites[(49-i+I,49-j)] = tuply[1]

				tuply = random.choice(lines)
				city[49-i+I][49+j] = 100-(int(tuply[0])/100)
				sites[(49-i+I,49+j)] = tuply[1]
	 		for J in xrange(dim):
	 			tuply = random.choice(lines)
				city[49-i][49-j+J] = 100-(int(tuply[0])/100)
				sites[(49-i,49-j+J)] = tuply[1]

				tuply = random.choice(lines)
				city[49+i][49-j+J] = 100-(int(tuply[0])/100)
				sites[(49-i,49-j+J)] = tuply[1]
		i += 1
		j += 1
		z += 1

with open('./heights', 'w') as f:
	f.write(city)

with open('./sites', 'w') as f:
	f.write(str(sites))