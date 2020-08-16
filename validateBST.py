# This is an input class. Do not edit.
#Divide and conquer and validate ALL subtrees
#every node in BST have value strictly greater than left nodes and values of right node
#left and right nodes must be BST
#start root node and validate all subtrees (go thru left and right sides )
#see if value is wrapped in min and max value range
#if each node btwn min and max value, call function on left/right and pass diff min/max
#if node has no child nodes, recursively dive up tree
#Time: O(N) -> number of nodes in tree b/c traversing every node in tree
#at root node, initialize min and max to -inf, +inf
#Space: calling each node recursively to see if each node btwn min/max O(d) (d is depth of tree)
#O(d) (d is length of longest branch, most space call stack)
#need helper function that takes min and max that we update
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	# Write your code here.
	return validateBstHelper(tree,float("-inf"),float("inf"))

		
def validateBstHelper(tree,minValue,maxValue):
		##if we hit leaf node having none value, we know we are in valid tree so return true
	if tree is None:
		return True
		##see node's value btwn min anx max value
	if tree.value < minValue or tree.value >= maxValue:
		return False
		##if node is valid, ensure both left and right subtrees are valid!
		##update max to tree.value b/c need to ensure less than max value
	leftIsValid = validateBstHelper(tree.left,minValue,tree.value)
	rightIsValid = validateBstHelper(tree.right,tree.value,maxValue)
	return leftIsValid and rightIsValid
