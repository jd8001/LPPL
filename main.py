import Population
import Individual
from pylab import *
import datetime

#t, a, b, tc, m, c, w, phi


inf = 2000.0
limits = ([0, 3], [.1, 1], [520, 850], [1, 2], [-1,1], [.1,2], [-1, 1])

x = Population.Population(limits, 20, 0.3, 1.5, .05, 4)
for i in range (5):
	x.Fitness()
	x.Eliminate()
	values = x.BestSolutions(3)
	for j in values:
		print j.PrintIndividual()
	x.Mate()
	x.Mutate()
	
	
x.Fitness()	
values = x.BestSolutions(3)
print "var dump"
try:
	print values[0].cof
except:
	print "nothing"
for x in values:
	print x.PrintIndividual()

x = values[0]
plot(x.getDataSeries()[0], x.getExpData())
scatter(x.getDataSeries()[0], x.getDataSeries()[1])
show()


	
	



# python "..\Documents\python\Genetic Algorithm\main.py"

		