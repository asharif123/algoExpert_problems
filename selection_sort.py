# Time: O(N^2), Space: O(1)
def selectionSort(array):

	for i in range(len(array)):
		min_index = i
		swap = 0
		for j in range(i+1,len(array)):
			if array[min_index] > array[j]:
				min_index = j
				swap += 1
		array[i],array[min_index] = array[min_index],array[i]
	return array
		
		
    
