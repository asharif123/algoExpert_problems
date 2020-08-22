def threeNumberSum(array, targetSum):
    # Write your code here.
	#sorting algo runs in Nlog(N) time and NO extra space and NOT change runtime since less than O(N^2)
	#find all possible triplets that will equal to target sum
	#triplet numbers should be ordered in ascending order
	#sort to find triplets in O(N^2) time using left/right pointers
	#iterate array once, assign pointers to currentNumber, left pointer to number right after current AND
	#right pointer to last value in array, currenSum = currentNumber + L + R
    #if currentSum == target Sum, add triplet values to final array AND
	#move pointers at same time since sum cant equal targetValue w/ starting value
	#if currentSum < targetSum, move leftpointer to right elif currentSum > targetSum, move rightpointer
	#if L > R, we increment currentValue and reset left/rightpointers
	#carry same operation
	#time: O(N^2) b/c iterating main array at least once AND at each number, use while to move left/right pointers and 
	#incrementing the currentNumber
	#space: O(N) b/c might store every number in array
	
	aray = array.sort()
	triplets = []
	##up to -2 b/c looking for triplets so we want left/right pointers and last currentNumber third value from end of array
	#also, both left and right pointers MUST be after current number so need to iterate upto third form last
	for i in range(len(array)-2):
		left = i+1
		right = len(array)-1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i],array[left],array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return triplets
