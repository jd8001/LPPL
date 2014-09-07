import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin_tnc
import random

import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
import datetime

def lppl (t,x):
	a = x[0]
	b = x[1]
	tc = x[2]
	m = x[3]
	c = x[4]
	w = x[5]
	phi = x[6]
	return a - (b*np.power(tc - t, m))*(1 + (c*np.cos((w *np.log(tc-t))+phi)))
	
def func(x):
	
	delta = [lppl(t,x) for t in DataSeries[0]]
	delta = np.subtract(delta, DataSeries[1])
	delta = np.power(delta, 2)
	return np.sum(delta)


class Individual:
	'base class for individuals'
	
	
	def __init__ (self, InitValues):
		self.fit = 0
		self.cof = InitValues
	
	def fitness(self):
		try:
			cofs, nfeval, rc = fmin_tnc(func, self.cof, fprime=None,approx_grad=True, messages=0)
			self.fit = func(cofs)
			self.cof = cofs
			
		except:
			
			#does not converge 
			return False
		
			
			
	def mate(self, partner):
		reply = []
		for i in range(0, len(self.cof)):
			if (random.randint(0,1) == 1):
				reply.append(self.cof[i])
			else:
				reply.append(partner.cof[i])
		
		return Individual(reply)
	def mutate(self):
		for i in range(0, len(self.cof)-1):
			if (random.randint(0,len(self.cof)) <= 2):
				#print "Mutate" + str(i)
				self.cof[i] += random.choice([-1,1]) * .5 * i
	
	def PrintIndividual(self):
		#t, a, b, tc, m, c, w, phi
		cofs = "A: " + str(round(self.cof[0], 3))
		cofs += "B: " + str(round(self.cof[1],3))
		cofs += "Critical Time: " + str(round(self.cof[2], 3))
		cofs += "m: " + str(round(self.cof[3], 3))
		cofs += "c: " + str(round(self.cof[4], 3))
		cofs += "omega: " + str(round(self.cof[5], 3))
		cofs += "phi: " + str(round(self.cof[6], 3))
		
		return "fitness: " + str(self.fit) +"\n" + cofs
		#return str(self.cof) + " fitness: " + str(self.fit)
	def getDataSeries(self):
		return DataSeries
	def getExpData(self):
		return [lppl(t,self.cof) for t in DataSeries[0]]

			
def fitFunc(t, a, b, tc, m, c, w, phi):
	return a - (b*np.power(tc - t, m))*(1 + (c*np.cos((w *np.log(tc-t))+phi))) 

	
SP = pd.io.data.get_data_yahoo('^GSPC', start=datetime.datetime(2012, 5, 1),end=datetime.datetime(2014, 5, 23))
time = np.linspace(0, len(SP)-1, len(SP))
close = [SP.Close[i] for i in range(len(SP.Close))]
global DataSeries
DataSeries = [time, close]
