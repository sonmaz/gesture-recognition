from signSection import *
import matplotlib.pyplot as plt
import mlpy

def extractInstance(filename):
	instances =[]
#	calculate the sections to distinguish examples providing the treshold
	secBeg, secEnd = signSection(filename, 0.3)
	f = open(filename, 'r')
	xs =[]
	ys =[]
	t = -1
	flag = 0;
	ex=0
	for line in f:
		t+=1
		a = line.split('\n')
		a = a[0].split('\t')
		if (len(a) > 1):
			temp = a[0].split(' ')
			z=float(temp[2])
#	finds the example in the file
			if(t > secBeg[ex] and t <secEnd[ex]):
				xs.append(float(temp[0]))
				ys.append(float(temp[1]))
				flag = 1
			else:
				if(flag == 1):
					flag = 0
					if(ex < len(secEnd)-1):
						ex+=1
					pair =(xs,ys)
					instances.append(pair)
#	returns the sequence for the example	
	#print instances[0][0]
	return instances