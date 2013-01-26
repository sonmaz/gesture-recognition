import numpy as np
class instance:
	sign =""
	x=[]
	y=[]
currentIndex = 0
ainstances=[]
signRange={}
allinstances={}
similMatr=[]
o = open('C:\Users\Sonmaz\Desktop\gestures\output.txt','w')#call the following function with the sign file and the example between 0 and 10

leetteers = ['a','b']
#allinstances['ax']=[]
#allinstances['ax'].append(xins)
#allinstances['ay']=[]
#allinstances['ay'].append(yins)

#convert python arrays to numpy arrays:
for letter in leetteers:
	xins, yins = signSection('C:\Users\Sonmaz\Desktop\gestures\graffiti-'+letter+'.txt', 0.3)
	pair=(currentIndex,currentIndex+len(xins))
	currentIndex+=len(xins)
	signRange[letter]=pair
	print 'sign length'
	print len(xins)
	print len(yins)
	
	for samp in range(len(xins)):
		temp = instance()
		temp.sign = letter
		temp.x=xins[samp]
		temp.y=yins[samp]
		ainstances.append(temp)

randflag=False
po=0	
for inst in range(0,len(ainstances)):
	temprow=[]
	po+=1
	print po 
	for instanc in range(0,len(ainstances)):
		#print(ainstances[inst].sign)
#		print inst
#		print instanc
#		
		npx1=arange(0)
		npy1=arange(0)
		npx2=arange(0)
		npy2=arange(0)		

		for index in ainstances[inst].x:
			npx1 = append(npx1, index)
		for index in ainstances[inst].y:
			npy1 = append(npy1, index)
		for index in ainstances[instanc].x:
			npx2 = append(npx2, index)
		for index in ainstances[instanc].y:
			npy2 = append(npy2, index)
		#calculate the distance for x and y
#		print 'distance'
		
		dtw = mlpy.Dtw(onlydist=False)	
		dx=dtw.compute(npx1, npx2)
		
#		if(randflag ==True):
#			p3 = plt.imshow(dtw.cost.T, interpolation='nearest', origin='lower')
#			p4 = plt.plot(dtw.px, dtw.py, 'r')
#			plt.show()
		dy=dtw.compute(npy1, npy2)
		print 'dy'
		print dy
#		randflag = True
		#write out the results
#		print 'file'
#		o.write(str(dx)+' ')
#		o.write(str(dy)+' ')
#		o.write(str(dx+dy))
#		o.write('\n')
	#	print str(dx+dy)
		temprow.append(str(dx+dy))
		similMatr.append(temprow)
	print similMatr[1]
for row in range(len(similMatr)):
	topten= findSmallest(similMatr[row])
	tp = 0.0
	for match in topten:
	#	print match
	#	print signRange
	#	print signRange['a'][0]
	#	print signRange['a'][0][1]
	#print match in range(signRange['a'][0],signRange['a'][1])
		for lett in leetteers:
			if row in range(signRange[lett][0],signRange[lett][1]):
				if match in range(signRange[lett][0],signRange[lett][1]):
					tp +=1
					print 'true'
				else:
					print 'False'
	#	print range(signRange['b'][0],signRange['b'][1])
	for lett in leetteers:
		if row in range(signRange[lett][0],signRange[lett][1]):
			pricision = tp/8
			recall = tp/(signRange[lett][1]-signRange[lett][0])
			o.write(lett)
			o.write('\n'+str(pricision))
			o.write('	')
			o.write(str(recall))
			o.write('\n')
