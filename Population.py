import Individual
import random
import numpy as np
import itertools

class Population:
	'base class for a population'
	LOOP_MAX = 1000
	
	def __init__ (self, limits, size, eliminate, mate, probmutate, vsize):
		'seeds the population'
		'limits is a tuple holding the lower and upper limits of the cofs'
		'size is the size of the seed population'
		self.populous = []
		self.eliminate = eliminate
		self.size = size
		self.mate = mate
		self.probmutate = probmutate
		self.fitness = []
		
		# Seeds = [np.linspace(a[0], a[1], a[2]) for a in limits]
		# for cofs in itertools.product(*Seeds):
			# self.populous.append(Individual.Individual(cofs))
		
		for i in range(size):
			SeedCofs = [random.uniform(a[0], a[1]) for a in limits]  
			self.populous.append(Individual.Individual(SeedCofs))
			
	def PopulationPrint(self):
		for x in self.populous:
			print x.cof
	def SetFitness(self):
		self.fitness = [x.fit for x in self.populous]
	def FitnessStats(self):
		#returns an array with high, low, mean
		return [np.amax(self.fitness), np.amin(self.fitness), np.mean(self.fitness)]
	def Fitness(self):
		counter = 0
		false = 0
		for individual in list(self.populous):
			print('Fitness Evaluating: ' + str(counter) +  " of " + str(len(self.populous)) + "        \r"),
			state = individual.fitness()
			counter += 1
			
			if ((state == False)):
				false += 1
				self.populous.remove(individual)
		self.SetFitness()
		print "\n fitness out size: " + str(len(self.populous)) + " " + str(false) 	
	def Eliminate(self):
		a = len(self.populous)
		self.populous.sort(key=lambda ind: ind.fit)
		while (len(self.populous) > self.size * self.eliminate):
			self.populous.pop()
		print "Eliminate: " + str(a- len(self.populous))
	def Mate(self):
		counter = 0
		while (len(self.populous) <= self.mate * self.size):
			counter += 1
			i = self.populous[random.randint(0, len(self.populous)-1)]
			j = self.populous[random.randint(0, len(self.populous)-1)]
			diff = abs(i.fit-j.fit)
			if (diff < random.uniform(np.amin(self.fitness), np.amax(self.fitness) - np.amin(self.fitness))):
				self.populous.append(i.mate(j))
			
			if (counter > Population.LOOP_MAX):
				print "loop broken: mate"
				while (len(self.populous) <= self.mate * self.size):
					i = self.populous[random.randint(0, len(self.populous)-1)]
					j = self.populous[random.randint(0, len(self.populous)-1)]
					self.populous.append(i.mate(j))
				
				
		print "Mate Loop complete: " + str(counter)
		
	def Mutate(self):
		counter = 0
		for ind in self.populous:
			if (random.uniform(0, 1) < self.probmutate):
				ind.mutate()
				ind.fitness()
				counter +=1
		print "Mutate: " + str(counter)
		self.SetFitness()
	
	def BestSolutions(self, num):
		reply = []
		self.populous.sort(key=lambda ind: ind.fit)
		for i in range(num):
			reply.append(self.populous[i])
		return reply;
		
		
		
	random.seed()