def findSmallest(arr):
	list=[]
	min = -1
	index= -1
	for i in range(8):
		min = -1
		index= -1
		for num in range(len(arr)):
			if(num not in list):
				if(min < 0):
					min = arr[num]
					index = num
				else:
					if min > arr[num]:
						min = arr[num]
						index = num
		list.append(index)
	return list
	
def findthresh(arr,threshold):
	list=[]
	min = -1
	index= -1
	for num in arr:
		if float(num[1]) < float(threshold):
			#print arr[num]
			list.append(num[0])
	return list