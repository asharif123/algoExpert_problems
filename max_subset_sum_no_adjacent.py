def maxSubsetSumNoAdjacent(array):
	#assume all positive integers?
    # find greatest sum of arrays that are NOT adjacent 
	# find smaller solns to find overall larger soln
	# in new array, store greatest sum that we can generate up until index of sum
	# use smaller solns to build up final soln
	# create array same length as input array and store greatest sum w NO adjacent numbers up until index where were storing sum
    
	#time: O(N), space: O(N)
	#Formula: either pick prev added value at maxsum (since CANT add to current index) OR 
	##take corr ind in array and add to second to prev added value in maxsum and
	#base case: at index = 0, return first value 
	#base case: at index = 1, return max of first or second value and add to maxSum array
	#Generate max sum from EACH index WITHOUT including adjacent values
	#    maxSum =[7,10,max(maxSum[i-2]+array[i],maxSum[i-1])]
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	
	#initialize maxSums (takes maxSums of each index value) by slicing thru original array
	#this ensures that maxSums will be same size as original array
	maxSums = array[:]
	maxSums[1] = max(array[0],array[1])
	#start from third value (second index)
	for i in range(2,len(array)):
		maxSums[i] = max(maxSums[i-1],maxSums[i-2]+array[i])
	return max(maxSums)
	##max(array[i]+maxSums[i-2],maxSums[i-1]
	##using O(N) space
	##[75,105,120,75,90.135]

	
