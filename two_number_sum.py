def twoNumberSum(array, targetSum):
    # Write your code here.
# 	do a foor loop of each value and subtract each value from target
# if the difference is in the list, we know that the number added to sum is in list and the pair equals to target
# note the values cannot be the same!
# O(n) time and O(n) space	
	for value in array:
		difference = targetSum - value
		if difference in array and difference != value:
			return [value,difference]
	return []
			
