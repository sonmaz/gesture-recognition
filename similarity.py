from numpy import *
import mlpy
from signSection import *
def similarity(treshold,instance1, instance2, sign1, sign2):
	x1=arange(0)
	y1=arange(0)
	x2=arange(0)
	y2=arange(0)
	b, e=signSection(treshold, sign1, instance1)
	t = -1
	
	for line in sign1:
		t+=1
		if(t > b):
			if(t<e):
				a = line.split('\n')
				a = a[0].split('\t')
				if (len(a) > 1):
					temp = a[0].split(' ')
					x1 = append(x1, float(temp[0]))
					y1 = append(y1, float(temp[1]))
			else:
				break
	b, e=signSection(treshold, sign2, instance2)
	t = -1
	for line in sign2:
		t+=1
		if(t > b):
			if(t<e):
				a = line.split('\n')
				a = a[0].split('\t')
				if (len(a) > 1):
					temp = a[0].split(' ')
					x2 = append(x2, float(temp[0]))
					y2 = append(y2, float(temp[1]))
			else:
				break		
	dtw = mlpy.Dtw()	
	dx=dtw.compute(x1,x2)
	dy=dtw.compute(y1, y2)
	o.write(str(dx))
	o.write('\n')
	o.write(str(dy))
	o.write('\n')
	o.write('====================================================================================')
	o.write('\n')