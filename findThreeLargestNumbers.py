def findThreeLargestNumbers(array):
	threeLargest = [None,None,None]
	for num in array:
		updateLargest(threeLargest,num)
	return threeLargest
	
def updateLargest(threeLargest,num):
#first check if threeLargest[index] is None or else cannot use greater than operator!
	if threeLargest[2] is None or num > threeLargest[2]:
		shiftAndUpdate(threeLargest,num,2)
			
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate(threeLargest,num,1)
		
	elif threeLargest[0] is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest,num,0)
		
def shiftAndUpdate(array,num,idx):
	for i in range(idx+1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i+1]
		
