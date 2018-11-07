from random import random as ran
import random
import math

def __init__(self):
	pass

def exp(a=1):
	"""Exponential random generator.

	It returns random numbers between 0 and inf with a exponential distribution with coefficent 'a'.
	"""
	return -math.log(ran())/a	
			
def boxmuller():
	"""Gaussian random generator, 2 independent values.

	It returns 2 random and independent numbers betwen -inf and inf with a gaussian 	disttribution with mean value 0 and deviation 1.
	"""
	x,y=ran(),ran()
	return math.sqrt(-2*math.log(x))*math.cos(2*math.pi*y),math.sqrt(-2*math.log(x))*math.sin(2*math.pi*y)

class MyRejectionFunction():
	"""Rejection with/o repetition method.

	It returns 1 random number with de distributios passed as a function using the rejection method, it can use rejection with/o repetition.
	"""
	def __init__(self):
		self.prevx=None

	def __call__(self,function,maxvalue,start=0,end=1,repetition=True):
		x=(end-start)*ran()+start
		if repetition==False or self.prevx==None:
			while function(x) < ran()*maxvalue:
				x=(end-start)*ran()+start
			self.prevx=x
			return x
		elif function(x) < ran()*maxvalue:
			return self.prevx
		else:
			self.prevx=x
			return x
rejection=MyRejectionFunction() #This method object works as a function to get randoms acording to the rejection w/o repetition algorithm.
				#It needs to be generelazed for multiple uses in a single program.(It has just one instance!)

def dynamicalmethods(function,prevx,method,N,delta=None,gaussian=False):
	"""Random number generator for N dimensions using Dynamical Methods
	
	It uses the dynamical method selected (Metropolis or Glauber) and it does one step (N iterations) taking randomly the value that actualizes each time. After one time step it returns the new N dimensional number. The method can choose between getting the new values followin the delta proces (1/sqrt(N)) or a gaussian distribution centered in the previous value. 
	"""

	for n in range(N):
		if delta==None:
			delta=1/math.sqrt(float(N))
		if gaussian==False:
			if N != 1:
				pos=int(N*ran())
				x=prevx[0:pos]+[prevx[pos]+delta*(2*ran()-1)]+prevx[pos+1:N]
			elif N==1:
				x=prevx+delta*(2*ran()-1)
		if gaussian==True:
			if N != 1:
				pos=int(N*ran())
				x=prevx[0:pos]+[random.gauss(prevx[pos],delta)]+prevx[pos+1:N]	
			elif N==1:
				x=random.gauss(prevx,delta)
		q=function(x)/float(function(prevx))
		if method == "metropolis":
			h=min(1,q)
		elif method == "glauber":
			h=q/(1+q)
		if ran()<=h:
			prevx=x[:]
	return prevx

