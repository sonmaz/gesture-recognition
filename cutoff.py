from string import ascii_lowercase
from signSection import *
import random
import matplotlib.pyplot as plt
import mlpy
from extractInstance import *
import numpy as np
from numpy import *
import mlpy
from sortIncreasing import *
class instance:
	sign =""
	x=[]
	y=[]
currentIndex = 0
trainD=[]
threshs={}
maxPrec = {}
bestthresh={}
precSum={}
precNum={}
signRange={}
allinstances={}
similMatr=[]
o = open('C:\Users\Sonmaz\Desktop\gestures\output.txt','w')#call the following function with the sign file and the example between 0 and 10
testD=[]
#instance1=extractInstance('C:\Users\Sonmaz\Desktop\gestures\graffiti-b.txt')
#instance2=extractInstance('C:\Users\Sonmaz\Desktop\gestures\graffiti-a.txt')
letters= ['b']
#allinstances['ax']=[]
#allinstances['ax'].append(xins)
#allinstances['ay']=[]
#allinstances['ay'].append(yins)
#convert python arrays to numpy arrays:
for letter in letters:
	xins, yins = signSection('C:\Users\Sonmaz\Desktop\gestures\graffiti-'+letter+'.txt', 0.3)
	for i in [0,1,2]:
		rand= random.uniform(0,len(xins))
		rand=abs(rand)
		testD.append([letter,xins.pop(rand),yins.pop(rand)])
	for i in range(len(xins)):
		trainD.append([letter,xins[i],yins[i]])
po=0
smallest = 100
largest = 0
for inst in range(len(trainD)):
	temprow=[]
	po+=1
	print po 
	for instanc in range(len(trainD)):
		#print(trainD[inst].sign)
#		print inst
#		print instanc
		npx1=arange(0)
		npy1=arange(0)
		npx2=arange(0)
		npy2=arange(0)		

		for index in trainD[inst][1]:
			npx1 = append(npx1, index)
		for index in trainD[inst][2]:
			npy1 = append(npy1, index)
		for index in trainD[instanc][1]:
			npx2 = append(npx2, index)
		for index in trainD[instanc][2]:
			npy2 = append(npy2, index)
		#calculate the distance for x and y
#		print 'distance'
		
		dtw = mlpy.Dtw(onlydist=False)	
		dx=dtw.compute(npx1, npx2)
#		p4 = plt.plot(trainD[11][1], trainD[11][2])
#		plt.show()		
#		if(randflag ==Tr[inst][ue):
#			p3 = plt.imshow(dtw.cost.T, interpolation='nearest', origin='lower')
#			p4 = plt.plot(dtw.px, dtw.py, 'r')
#			plt.show()
		dy=dtw.compute(npy1, npy2)
#		randflag = True
		#write out the results
#		print 'file'
#		o.write(str(dx)+' ')
#		o.write(str(dy)+' ')
#		o.write(str(dx+dy))
#		o.write('\n')
	#	print str(dx+dy)
		temprow.append([trainD[instanc][0],str(dx+dy)])
		if dx+dy < smallest:
			smallest = dx+dy
		if dx+dy>largest:
			largest = dx +dy
	similMatr.append([trainD[inst][0],temprow])
print similMatr[1]
print smallest
print largest
smallest = float(str(smallest)[0] + str(smallest)[1] + str(smallest)[2])
largest = float((str(largest))[0] + (str(largest))[1] + (str(largest))[2] +(str(largest))[3]+(str(largest))[4])+0.001
print 'small + large'
print smallest
print largest
ind = smallest
while ind <= largest:
	o.write('=====================================================\n')
	o.write('threshold: '+str(ind)+'\n')
	o.write('=====================================================\n')
	for row in similMatr:
		topten= findthresh(row[1],ind)
		if(len(topten) == 0):
			continue
		#print row[1]
		#print 'topten'
		#print topten
		tp = 0.0
		pos=0
		for ro in row[1]:
			if row[0] == ro[0]:
			#	print row[0]
			#	print ro[0]
				#print 'print'
				pos +=1
	#	print 'pooooooooooooooooooooooooooooooos'
	#	print pos
		for match in topten:
		#	print match
		#	print signRange
		#	print signRange['a'][0]
		#	print signRange['a'][0][1]
		#print match in range(signRange['a'][0],signRange['a'][1])
			if match == row[0]:
				tp +=1
			#	print 'true'
			#else:
			#	print 'False'
		#	print range(signRange['b'][0],signRange['b'][1])
		precision = tp/len(topten)
		recall = tp/pos
		fmeasure = 2*precision*recall/(precision + recall)
		if row[0] not in precSum:
			precSum[row[0]]=0
			precNum[row[0]]=0
	#		bestthresh[row[0]]=0
	#		maxPrec[row[0]]=0
		precSum[row[0]] += fmeasure
		precNum[row[0]] += 1
		
	#	o.write(row[0])
	#	o.write('\n'+str(precision))
	#	o.write('	')
	#	o.write(str(recall))
	#	o.write('\n')
	for ky in precSum.keys():
		if ky not in threshs:
			threshs[ky]=0
		if ky not in bestthresh:
			bestthresh[ky]=0
	for i in range(len(precSum)):
	#	print precSum[(precSum.keys())[i]]
	#	print precNum[(precNum.keys())[i]]
		o.write((precSum.keys())[i] + ' ' + str(precSum[(precSum.keys())[i]]/precNum[(precNum.keys())[i]])+'\n')
		if(precSum[(precSum.keys())[i]]/precNum[(precNum.keys())[i]] > threshs[(precSum.keys())[i]]):
			threshs[(precSum.keys())[i]] = precSum[(precSum.keys())[i]]/precNum[(precNum.keys())[i]]
			bestthresh[(precSum.keys())[i]]=ind
	ind += 0.001
o.write('best thresholds:\n')
for i in range(len(threshs)):
	o.write(threshs.keys()[i]+':	'+ str(bestthresh[threshs.keys()[i]])+ '	'+str(threshs[threshs.keys()[i]])+'\n')
#print threshs
#print bestthresh


#====================================================================testing========================================================

currentIndex = 0
precSum={}
precNum={}
signRange={}
#allinstances={}
similMatr=[]
for inst in range(len(testD)):
	temprow=[]
	po+=1
	print po 
	for instanc in range(len(testD)):
		#print(testD[inst].sign)
#		print inst
#		print instanc
		npx1=arange(0)
		npy1=arange(0)
		npx2=arange(0)
		npy2=arange(0)		

		for index in testD[inst][1]:
			npx1 = append(npx1, index)
		for index in testD[inst][2]:
			npy1 = append(npy1, index)
		for index in testD[instanc][1]:
			npx2 = append(npx2, index)
		for index in testD[instanc][2]:
			npy2 = append(npy2, index)
		#calculate the distance for x and y
#		print 'distance'
		
		dtw = mlpy.Dtw(onlydist=False)	
		dx=dtw.compute(npx1, npx2)
#		p4 = plt.plot(testD[11][1], testD[11][2])
#		plt.show()		
#		if(randflag ==Tr[inst][ue):
#			p3 = plt.imshow(dtw.cost.T, interpolation='nearest', origin='lower')
#			p4 = plt.plot(dtw.px, dtw.py, 'r')
#			plt.show()
		dy=dtw.compute(npy1, npy2)
#		randflag = True
		#write out the results
#		print 'file'
#		o.write(str(dx)+' ')
#		o.write(str(dy)+' ')
#		o.write(str(dx+dy))
#		o.write('\n')
	#	print str(dx+dy)
		temprow.append([testD[instanc][0],str(dx+dy)])
	similMatr.append([testD[inst][0],temprow])
print similMatr[1]
for row in similMatr:
	topten= findthresh(row[1],bestthresh[row[0]])
	if(len(topten) == 0):
		continue
	#print row[1]
	#print 'topten'
	#print topten
	tp = 0.0
	pos=0
	for ro in row[1]:
		if row[0] == ro[0]:
		#	print row[0]
		#	print ro[0]
			#print 'print'
			pos +=1
#	print 'pooooooooooooooooooooooooooooooos'
#	print pos
	for match in topten:
	#	print match
	#	print signRange
	#	print signRange['a'][0]
	#	print signRange['a'][0][1]
	#print match in range(signRange['a'][0],signRange['a'][1])
		if match == row[0]:
			tp +=1
		#	print 'true'
		#else:
		#	print 'False'
	#	print range(signRange['b'][0],signRange['b'][1])
	precision = tp/len(topten)
	recall = tp/pos
	fmeasure = 2*precision*recall/(precision + recall)
	if row[0] not in precSum:
		precSum[row[0]]=0
		precNum[row[0]]=0
#		bestthresh[row[0]]=0
#		maxPrec[row[0]]=0
	precSum[row[0]] += fmeasure
	precNum[row[0]] += 1
	
#	o.write(row[0])
#	o.write('\n'+str(precision))
#	o.write('	')
#	o.write(str(recall))
#	o.write('\n')
o.write('testing result:\n')
for i in range(len(precSum)):
#	print precSum[(precSum.keys())[i]]
#	print precNum[(precNum.keys())[i]]
	o.write((precSum.keys())[i] + ' ' + str(precSum[(precSum.keys())[i]]/precNum[(precNum.keys())[i]])+'\n')
#	if(precSum[(precSum.keys())[i]]/precNum[(precNum.keys())[i]] > threshs[(precSum.keys())[i]]):
#		threshs[(precSum.keys())[i]] = precSum[(precSum.keys())[i]]/precNum[(precNum.keys())[i]]
#		bestthresh[(precSum.keys())[i]]=ind

