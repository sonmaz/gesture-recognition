from string import ascii_lowercase
from signSection import *
import matplotlib.pyplot as plt
import mlpy
import numpy as np
from numpy import *
import mlpy
class instance:
	sign =""
	x=[]
	y=[]
currentIndex = 0
ainstances=[]
signRange={}
allinstances={}
similMatr=[]
#o = open('C:\Users\Sonmaz\Desktop\gestures\output.txt','a')#call the following function with the sign file and the example between 0 and 10

#instance1=extractInstance('C:\Users\Sonmaz\Desktop\gestures\graffiti-b.txt')
#instance2=extractInstance('C:\Users\Sonmaz\Desktop\gestures\graffiti-a.txt')

#allinstances['ax']=[]
#allinstances['ax'].append(xins)
#allinstances['ay']=[]
#allinstances['ay'].append(yins)
#convert python arrays to numpy arrays:

xins, yins = signSection('C:\Users\Sonmaz\Desktop\gestures\graffiti-z.txt', 0.3)
print len(xins)
num = 9
p4 = plt.plot(xins[num],yins[num])
plt.show()