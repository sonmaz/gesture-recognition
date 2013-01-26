
import matplotlib.pyplot as plt

def signSection(filename,treshold):
	f = open(filename, 'r')
	startFlag=0
	secBeg =[]
	secEnd=[]
	xs=[]
	ys=[]
	xinstances=[]
	yinstances=[]
	firstSec =0
	t = -1
	endflag =0
	o = open('C:\Users\Sonmaz\Desktop\gestures\output.txt','a')#call the following function with the sign file and the example between 0 and 10

# comparing all the z values with the treshold to find the beginning and the end of the sections of the symbols
	for line in f:
		a = line.split('\n')
		a = a[0].split('\t')
		t += 1
		if (len(a) > 1):
			temp1 = a[0].split(' ')
			temp2 = a[1].split(' ')
			z=(float(temp1[2])+float(temp2[2]))/2
			x=(float(temp1[0])+float(temp2[0]))/2
			y=(float(temp1[1])+float(temp2[1]))/2
			if(z > treshold):
				if(startFlag == 0):
					startFlag = 1
					secBeg.append(t)
					xs=[]
					ys=[]
				xs.append(x)
				ys.append(y)
				#o.write(line)
			else:
				if(startFlag == 1):
					startFlag = 0
					secEnd.append(t)
				#	o.write('/////////////////////////////////////////////////////////////////////////')
					xinstances.append(xs)
					yinstances.append(ys)	
	if(len(secBeg) - 1 == (len(secEnd))):
		secEnd.append(t)
		xinstances.append(xs)
		yinstances.append(ys)
	for pl in range(len(secBeg)):
		print secBeg[pl]
		print secEnd[pl]
		print '-----------------------'
		#	plt.plot(xinstances[1], yinstances[1])
#	plt.show()
	#print xinstances[0][0]
#	returns the beginning and the end of sign sections
	return xinstances, yinstances