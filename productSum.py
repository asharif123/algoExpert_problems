# Tip: You can use the type(element) function to check whether an item
#special array -> array that either has integers or other special arrays
# is a list or an integer.
#Time: O(n), Space: O(d) (because we are using recursive calls to increase depth each time we pass array and using space on call stacks!)
#O(d) is depth of your arrays
#O(n) represents all elements in array INCLUDING elements in special arrays and NOT just every individual element in the array
#HINT: if there are subarrays in array, sign that it involves recursion!
def productSum(array,multiplier=1):
    
    # iterate through every value in the array
	# set total to 0 each time we call the recursive function when we hit special array
    total = 0
    for value in array:
        if type(value) == int:
            total += value
        else:
            total += productSum(value,multiplier+1)
#if at end of array, return total*multiplier
    return total*multiplier
			
			


print(productSum([5,2,[7,-1],3,[6,[-13,8],4]]))
			
