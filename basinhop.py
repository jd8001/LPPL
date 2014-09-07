from pylab import *
import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin_tnc
import random
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
import datetime

#a, b, tc, m, c, w, phi

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
	return np.average(delta)
	
	
	
SP = pd.io.data.get_data_yahoo('^GSPC', start=datetime.datetime(2012, 5, 1),end=datetime.datetime(2014, 5, 23))
time = np.linspace(0, len(SP)-1, len(SP))
close = [SP.Close[i] for i in range(len(SP.Close))]
global DataSeries
DataSeries = [time, close]


limits = ([0, 10], [0.01, 10], [520, 850], [1, 2], [-1,1], [0,2], [-1, 1])
#print str(func([1,1,600,1.5,.5,1,.5]))
cofs, nfeval, rc = fmin_tnc(func, [1.5, .5, 600, 1.5, 0, 1, 0], fprime=None,approx_grad=True)
print cofs
print nfeval
print "value of func: " + str(func(cofs))
values = [lppl(t,cofs) for t in DataSeries[0]]
plot(DataSeries[0], values)
scatter(DataSeries[0], DataSeries[1])
show()
 