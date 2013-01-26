#from numpy.fft import fft
#from scipy import fftpack
from svmutil import *
from numpy.fft import fft
from numpy import *
from string import ascii_lowercase
from signSection import *
import random
import matplotlib.pyplot as plt
import mlpy
from extractInstance import *
import numpy as np
from numpy import *
from mlpy import *
from sortIncreasing import *

class feature:
	mean = 0
	energy = 0
	entropy = 0
	correlation = 0
class Gesture:
	frame1=[]
	frame=[]
	name =0
	features=[]
	def __init__(self):
		self.frame1=[]
		self.frame = []
		self.features=[]
gesturesT=[]
gesturesD=[]
trainD=[]
testD=[]
letters= ['e','k']
n=10
trSeg=[]
tsSeg=[]
def svmexperiment():
	o = open('C:\Users\Sonmaz\Desktop\gestures\output.txt','a')#call the following function with the sign file and the example between 0 and 10
	for letter in letters:
		xins, yins = signSection('C:\Users\Sonmaz\Desktop\gestures\graffiti-'+letter+'.txt', 0.3)
		for i in [0,1,2]:
			rand= random.uniform(0,len(xins))
			rand=int(floor(rand))
			testD.append([letter,xins.pop(rand),yins.pop(rand)])
		for i in range(len(xins)):
			trainD.append([letter,xins[i],yins[i]]) 	
#===================================================================end of reading the file==========================================	
	
	for td in testD:
		tmp = Gesture()
		tmp.name = td[0]
		l = len(td[1])
		ls = (l / (n+1))
		for i in range(0, n):
			tmp.frame1.append([td[1][i * ls : (i+1) * ls],td[2][i * ls : (i+1) * ls]])
		for fr1 in range(len(tmp.frame1)-1):
			if len(tmp.frame1[fr1][0]+tmp.frame1[fr1+1][0]) < ls:
				break
			if len(tmp.frame1[fr1][1]+tmp.frame1[fr1+1][1]) < ls:
				break
			tmp.frame.append([tmp.frame1[fr1][0]+tmp.frame1[fr1+1][0],tmp.frame1[fr1][1]+tmp.frame1[fr1+1][1]])
		for fr in tmp.frame:
			trans=[]
			trans.append(fft.fft(fr[0]))
			trans.append(fft.fft(fr[1]))
			
			sum1= 0
			sum2 = 0
			tmp.features.append(abs(trans[0][0]))
			tmp.features.append(abs(trans[1][0]))
			for i in range(len(trans[0])):
				sum1 += trans[0][i]*trans[0][i]
			for i in range(len(trans[1])):
				sum2 += trans [1][i]*trans[1][i]
			tmp.features.append(int(abs(sum1)/(2*ls - 1)))
			tmp.features.append(int(abs(sum2)/(2*ls - 1)))

		while len(tmp.features) < (n+1):
			tmp.features.append(0)
		print 'faaaaaa'
		print len(tmp.features)
		gesturesD.append(tmp)
	for tr in trainD:
		tmp = Gesture()
		tmp.name = tr[0]
		l = len(tr[1])
		ls = l / (n+1)
		for i in range(0, n):
			tmp.frame1.append([tr[1][i * ls : (i+1) * ls],tr[2][i * ls : (i+1) * ls]])		
			
		for fr1 in range(len(tmp.frame1)-1):
			if len(tmp.frame1[fr1][0]+tmp.frame1[fr1+1][0]) < ls:
				break
			if len(tmp.frame1[fr1][1]+tmp.frame1[fr1+1][1]) < ls:
				break
			tmp.frame.append([tmp.frame1[fr1][0]+tmp.frame1[fr1+1][0],tmp.frame1[fr1][1]+tmp.frame1[fr1+1][1]])		
		for fr in tmp.frame:
			trans=[]
			#print fr[0]
			trans.append(fft.fft(fr[0]))
			trans.append(fft.fft(fr[1]))
			sum1= 0
			sum2 = 0
			tmp.features.append(abs(trans[0][0]))
			tmp.features.append(abs(trans[1][0]))
			for i in range(len(trans[0])):
				sum1 += trans[0][i]*trans[0][i]
			for i in range(len(trans[1])):
				sum2 += trans[1][i]*trans[1][i]
			tmp.features.append(int(abs(sum1)/(2*ls - 1)))
			tmp.features.append(int(abs(sum2)/(2*ls - 1)))
		print 'taaaa'
		while len(tmp.features) < (n+1):
			tmp.features.append(0)
		print len(tmp.features)
		gesturesT.append(tmp)
#============================================================================end of feature extraction	
	truelabels=[]
	attributes=[]
	labels=[]
	testAtr=[]
	
	for ge in gesturesT:
		tempAtr=[]
		for fe in ge.features:
			tempAtr.append(fe)
		attributes.append(tempAtr)
		if(ge.name == 'e'):
			labels.append(-1)
		else:
			labels.append(1)
		
	for ge in gesturesD:
		tempAtr=[]
		for fe in ge.features:
			tempAtr.append(fe)
		testAtr.append(tempAtr)
		if(ge.name == 'e'):
			truelabels.append(-1)
		else:
			truelabels.append(1)
	#print attributes	
	attributes = array(attributes)
	print attributes
	mysvm = Svm()
	#print testAtr
	testAtr=array(testAtr) 
	print 'sep'
	labels=array(labels)
	#labels = array([-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1])
	mysvm.compute(attributes,labels)
	print testAtr
	predictedlabels = mysvm.predict(testAtr)
	o.write('\n'+str(truelabels))
	o.write(str(predictedlabels))
	correct = 0
	for la in range(len(truelabels)):
		if truelabels[la] == predictedlabels[la]:
			correct += 1
	print correct
svmexperiment()