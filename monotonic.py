
##time: O(N) time, space: O(1)
##monotonic: array must EITHER be linearly increasing OR linearly decreasing
def isMonotonic(array):

##if monotonically increasing, confirm if monotonically increasing thruout array!
    for i in range(1,len(array)-1):
		if (array[i] < array[i-1]):
			if array[i] < array[i+1]:
				return False
				
##if monotonically decreasing, confirm if monotonically decreasing thruout array!
		elif (array[i] > array[i-1]):
			if array[i] > array[i+1]:
				return False
    return True
