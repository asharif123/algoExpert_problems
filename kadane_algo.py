#subarray -> array within array
#find largest sum in subarray
#maxSum = [1,max(-3,-3+1),max(2,2-3,2-3+1),max(1,1+2,1+2-3,1+2-3+1),max(-1,-1+1,-1+1+2,-1+1+2-3,-1+1+2-3+1)]
#above in O(n^2)
#O(n) time and O(1) space soln:
#use dynamic programming:
#for first index, greatest sum is just first index
#to find max sum at index, either take max sum at prev index and add to current index, or use current number
#maxEndinghere = max(maxEndingHere+num[i] OR num[i])
#array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

def kadanesAlgorithm(array):
    # Write your code here.
	
	maxEndingHere = array[0] #3
	maxSoFar = array[0] #3
	for num in array[1:]:
		maxEndingHere = max(num,maxEndingHere+num) #8,-1,1,4,2,5,9,16,18,9,15,18,19,14,18
		maxSoFar = max(maxEndingHere,maxSoFar)
	return (maxSoFar)
