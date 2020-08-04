#Time: O(n^2), Space: O(1)
def insertionSort(array):
	value = 1
	while value < len(array):
		for i in range(value,0,-1):
			if array[i] < array[i-1]:
				array[i],array[i-1] = array[i-1],array[i]
		value += 1
	return array
		
