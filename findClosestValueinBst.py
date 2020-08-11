# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

##keep track of closest value to target using closest
def findClosestValueInBst(tree, target, closest=float('inf')):
	##Using recursive approach
    # Time: Olog(n)
	# Space: O(1)
	# Worst case: O(n)
	##keep track of closest variable, function take in closest value (using recursive function)
	## tree, target and closest value
	
	currentNode = tree
	while currentNode is not None:
	##else compute abs difference of abs(number - target) and keep track of closest
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		##once we have taken first step of finding closest, compare target to current node value and 
		##decide which part of the tree to explore
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			return closest
	return closest
		
    



