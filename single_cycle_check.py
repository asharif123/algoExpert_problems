def hasSingleCycle(array):

	##ask interviewer if we will have negative integers or decimal values
    #determine if list has single cycle
	#each integer represents number of jumps in array
    #single cycle means that we will return to first number and visit every number exactly 1
	#Ex: [2,3,1,-4,-4,2] (start at 2 and move forward by 2, at 1, move by 1, at -4, end of array ->)
	#now at 3, now at -4, and back to first 2
	#[1,-1,1,-1] is independent loop that goes back and forth

	#visit jump through n elements (n = 6), jump thru n elements, if we rearrive at first element, we got cycle
	#[2,3,1,-3,-4,2] returns to 2 WITHOUT visiting all elements
	#GOAL: visit all elements and ensure you return to main array
	#visit n elements of array, visit more than 1 element and ensure NOT 1 < n < 6 or n == 6
	#Time = O(n), Space = O(1)
	#ensure you visit exactly n elements and return to starting value
	
	##single check FAILS under following conditions:
	##if not all n elements have been visited (ex: start at first element but we return to initial index)
	##if all n elements have been visited but we DON'T  return to starting value
	
	##iterate thru n elements
	numElementsVisited = 0
	
	##keep track of index we're at
	currentIdx = 0
	
	while numElementsVisited < len(array):
	
	##if not all n elements have been visited (ex: start at first element but we return to initial index)
		if numElementsVisited > 0 and currentIdx == 0:
			return False
		numElementsVisited += 1
		
		#jump thru all elements
		currentIdx = getNextIdx(currentIdx, array)
		
	##see whether we have visited ALL elements AND have returned to starting index!
	return currentIdx == 0	
	
def getNextIdx(currentIdx,array):

##determine how many jumps needed
	jump = array[currentIdx]	
	
	##if we go past bounds, ensure we wrap around using mod operator
	nextIdx = (currentIdx + jump) % len(array)
	
	##handle edge case where currentIdx may be negative!
	return nextIdx if nextIdx >= 0 else nextIdx + len(array) #ensures that you move forward equivalent to rotating backwards!

	
