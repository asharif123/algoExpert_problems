def binarySearch(array, target):
    # Write your code here.
	#Compare x with the middle element.
	#If x matches with the middle element, we return the mid index.
	#Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
	#Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
    #NOTE: if array is sorted, strong indicator ta
	##Time: Olog(n) b/c we are eliminating array by half EACH time we try to find target value
	##Space: O(1)
	
	low = 0
	high = len(array)-1
	##if we reach list having no elements, we know target was NOT found!
	while low <= high:
	#//2 USED to round down incase if we have decimal after dividing low+high
		mid = (low+high)//2
		if target == (array[mid]):
			return mid
		##if target is greater than mid
		elif target > (array[mid]):
			low = mid+1
		elif target < (array[mid]):
			high = mid-1
			
		
	return -1
	
