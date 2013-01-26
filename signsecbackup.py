def signSection(treshold,f,ex):
	#f = open('C:\Users\Sonmaz\Desktop\gestures\graffiti-b.txt', 'r')
	startflag=0
	secBeg =[]
	secEnd=[]
	firstSec =0
	t = -1
	endflag =0
	for line in f:
		a = line.split('\n')
		a = a[0].split('\t')
		t += 1
		if (len(a) > 1):
			temp = a[0].split(' ')
			z=float(temp[2])
			if (z < 0.3):			
				if(endflag==0):
					if(len(secBeg)>0):
						#zs.append(t)
						secEnd.append(t)
					#else:
						#zs.append(1)
					endflag=1
					startflag=0
				#else:
				#	zs.append(1);	
	#			if(ex == 1):
	#				plt.plot(xs, ys)
	#				plt.show()
				#xs=[]
				#ys =[]
				
				continue
	#		ex +=1
			#xs.append(float(temp[1]))
			#ys.append(float(temp[0]))
			endflag = 0
			if startflag ==0:
				startflag =1
				if(firstSec == 0):
			#		zs.append(1)
					firstSec =1
				else:
			#		zs.append(t)
					secBeg.append(t)
				
			#else:
			#	zs.append(0)
	#ti.append(t)
	#zs.append(3.1)		
	#plt.plot(ti, zs)
	#plt.show()

	print len(secBeg)
	print len(secEnd)	
	for sb in secBeg:
		print sb
	print 'seperator'
	for se in secEnd:
		print se
	#	print secEnd[i]
#	f.close()
	return secBeg[ex], secEnd[ex]	
	#dtw = mlpy.Dtw()
	#d = dtw.compute(x, y)
	#fig2 = plt.figure(2)
	#p3 = plt.imshow(dtw.cost.T, interpolation='nearest', origin='lower', onlydist=False)
	#p4 = plt.plot(dtw.px, dtw.py, 'r')
	#plt.show()