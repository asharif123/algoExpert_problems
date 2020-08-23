def fourNumberSum(array, targetSum):
    # array = [7,6,4,-1,1,2]
	# array = [-1,1,2,4,6,7]
	# find all quadruplets that sum up to targetSum, can be solved in O(N^4)
	#quadruplet can be expressed as pair of numbers
	#can turn into pair of numbers (ex: x,y,z,k, x+y -> p and z+k -> q)
	#find sums of ALL pairs in array (p,q) and find sum of p+q that sums to target
	#p,q represent 2 sums, 2 number sum problem
	#store number in hash table -> {p: [x,y] sum bunch pair of numbers}
	#{P: [x,y]}
	#keep track of which numbers were used to P or Q
	#DO NOT doublecout pairs or quadruplets
	#EX: [7,6,4,-1,1,2], targetSum = 16
	#{13: [[7,6]], 3: [[4,-1]], 10: [[6,4]], 6: [[7,-1]]}, doublecounted quadruplet
	#kept track of same quadruplet twice
	
	#in 2 number sum, iterate thru each value and see if target - value is in array and return
	#[value,difference]
	#first iterate one by one, first inner for loop that iterates AFTER current number and get sum of currentNumber + number that comes after AND
	#see if P sum value diff of targetSum - P is in hash table, if NOT, we will NOT add that sum to hash table yet
	#iterate numbers before current number and generate Q that we add to hash table
	#EX: [7,6,4,-1,1,2], targetSum = 16
	#[[7,6,4,-1],[7,6,1,2]]
	#{13: [[7,6],[4,-1]], 11: [[7,4]], 10: [[6,4]], 8: [[7,-1]], 5: [[6,-1]], 3: [[4,-1]], 6: [[7,1]],  }
	#start at 7,iterate via every number after 7, each take sum to current number, then diff btwn target and sum
	#if diff NOT in hash table, move on and DO NOT add sum to hash table 
	#at first value, NOTHIG exists in hash table so move on to second value
	#now at 6, iterate via all after 6 and see if in hash table, none of the diff in hash table so NOW
	#iterate all values before 6 (7), 6+7 = 13 and ADD to hash table {13: [[7,6]]}
	#ONLY add sum to hash table when we reach value after first value
	#if diff already in hash table, (Ex: 16+(4-1) = 13),  every single pair at value in hash table should be combined with pair numbers from P and added to quadruplets
	#so now [7,6,4,-1]
	#if Q value already in hashtable, add another list pair to the corr key!
	#stop when we reach last value as there are no values after last
	#This approach works b/c ensures we DONT add duplicate quadruplets by adding pair of vlaues to hash table STARTING at second value
	# Time (avg): O(N^2) using 1 for loop to iterate all values in array and inside doing 2 other for loops (one after current AND one before current)
	#start one value after first and one before first
	# Space: O(N^2) number of quadruplets not sure how many there will be, we have N squared pairs

#######################################################################################################	
	##initialize hash table to store sum of every pair in array
	allPairSums = {}
	
	quadruplets = []
	
	#start iterating outer for loop skip first and final values b/c have nothinf for first value in hash table and
	#last value has NO values to iterate
	for i in range(1,len(array)-1):
		for j in range(i+1,len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if difference in allPairSums:
			
			##iterate thru all pairs in hash table
			##Ex: {13: [[7,6]]}
				for pair in allPairSums[difference]:
					quadruplets.append(pair + [array[i], array[j]])
		
		##add values that come before currentvalue to hash table
		for k in range(0,i):
			currentSum = array[i] + array[k]
			if currentSum not in allPairSums:
				allPairSums[currentSum] = [[array[k], array[i]]]
			##else if sum already in hashtable, add the pair to current pair having sum
			else:
				allPairSums[currentSum].append([array[k], array[i]])
	return quadruplets
