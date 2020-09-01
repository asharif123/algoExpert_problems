def largestRange(array):
    # take array of integers and return LARGEST range that can be formed! (return as length 2)
	# range does NOT need to be next to one another but MUST be comtained somewhere in array
	# sorting NOT most optimal soln
	# OTHER SOLN: access each numbers in input array and store in hash table
	# ex: [1,11,3,0,15,5,2,4,10,7,12,6]
	# { 1:F  2:F 6:F }
	#   11:F   4:F  5:F 
	#   3:F   10:F
	#  0:F  7:F 
	# 15:T  12:F 
	# }
	#iterate and start at 1, explore range where 1 is located in that's in array by traversing all values smaller than 1 and see if contained in hash table AND
	#iterate all values greater than 1 and see if in hash table
	#ex: 1, 0 since 0 in hash table so can be accessed in constant time, then -1 (not in hash table so erase -1)
	#so lower range goes from 0 and 1, now go to right of 1 -> 2, 2 is in our hash table so now we have 0 1 2
	#3 in hash table so 0 1 2 3, 4 in hash table, 5, 6 and 7 are all in hash table and array 
	#get to 8 and 8 NOT in hash table so final range is [0,1,2,3,4,5,6,7] and store it in top
	#now start at 11, 10 in hash table, 9 NOT there, right 12 in hash table and no 13 [10 11 12] store in potential ranges
	# now at 3, we would get exact same range and repeating SO have every number map to boolean 
    # if number has been discovered change to false so if 3 is marked as F, skip it!
	# when we hit 15, mark it as F and numbers before and after (none exist in hash table) so [15]
	# final range is [0,1,2,3,4,5,6,7]
	# time: O(N) b/c iterate once thru array put in hash table reiterate and go around about one time!
	# space: O(N) b/c storing every number in hash table plus range we store does NOT have extra N space
	
	##keep track of largest range (hold first and length)
	bestrange = []
	
	##hold value of largest length of best range and compare if largest
	longestLength = 0
	
	#create hash table that holds number AND boolean on whether visited or NOT!
	nums = {}
	
	for num in array:
	##initialize every UNVISITED number as True
		nums[num] = True
	
	##go again thru array and see if visited or not from hash table
	for num in array:
	
	##if false, number has been visited so SKIP!!
		if not nums[num]:
			continue
	
	##if num VISITED, set to False
		nums[num] = False
		currentLength = 1
		
		##see if left AND right are in hash table
		left = num - 1
		right = num + 1
		
		##while values to the left of current value are in the array
		while left in nums:
			nums[left] = False
			currentLength += 1
		##decrement left to point is no longer in nums (leftmost number)
			left -= 1
			
		##while values to the right of current value are in the array	
		while right in nums:
			nums[right] = False
			currentLength += 1
			right += 1
			
		##see if our new range qualifies best range by comparing currentLenght and then update the bestRange
		if currentLength > longestLength:
			longestLength = currentLength
			##decrement left no longer in num, ex if range is [0,7] left => -1 and NOT in hash table so need to add 1 to compensate
			##same for right, subtract 1
			
			##bestrange is left extremity of range and right extremity
			bestrange = [left+1, right-1] ##DO NOT APPEND! we want to update both values EACH time
			
	return bestrange
		
		
	
	
	
