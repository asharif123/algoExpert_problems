#Bubble Sort: Time: O(N^2), Space: O(1)
def bubbleSort(array):
    iterate = 0
	while (iterate < len(array)):
	#count number of swaps, if no swap occurs after iterating, break out of loop!
		swap = 0
		for i in range(len(array)-1-iterate):
			if (array[i] > array[i+1]):
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
				swap += 1
				
		iterate += 1
		if swap == 0:
			break
		
	return array
   
