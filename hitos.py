import numpy as np
from randomdistributions import boxmuller as rang
from randomdistributions import exp
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from plots import drawhistogram as hs

data=[rang() for i in range(10000)]
y1,binEdges1=np.histogram(data,bins=50,density=True)
bincenters1 =0.5*(binEdges1[1:]+binEdges1[:-1])
err1=[np.sqrt(x/float(len(data))*(1-x))/float(np.absolute(float(binEdges1[0])-float(binEdges1[1]))) for x in iter(y1)]
x=np.linspace(-4,4,1000)
plt.figure()
plt.plot(x,mlab.normpdf(x,0,1))
hs(data)
plt.savefig("gaussWerr.png")

data2=[exp() for i in range(10000)]
y2,binEdges2=np.histogram(data2,bins=50,density=True)
bincenters2 =0.5*(binEdges2[1:]+binEdges2[:-1])
err2=[np.sqrt(x/float(len(data))*(1-x))/float(np.absolute(float(binEdges2[0])-float(binEdges2[1]))) for x in iter(y2)]
x2=np.linspace(0,6,1000)
plt.figure()
plt.plot(x2,np.exp(-x2))
hs(data2)
plt.savefig("expWerr.png")


