# This is the class of the input root. Do not edit it.
# Use depth first search: uses a stack that we create or recursively
# LIFO, goes deep into path
# Used in backtracking, complete search, finding all the paths
# go thru each value and end at leaf nodes (nodes at bottom of tree)
#Time: O(n) b/c have to traverse thru every value in node and adding value at that node
#Space (using recursive operation): O((N)) (b/c eliminating half of nodes each time) and:
#NEVER exceeding N number of items in branch sum
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#takes in root of binary tree and every node has value or integer and left/right value!!
##Time: O(N) b/c traversing all N nodes, Space: O(N) b/c we're returning list of branch sums having number of branches in binary tree
def branchSums(root):
	#keep track of running list of branch sums
	sums = []
	runningSum = 0
	##call recursively on each root value
	calculateBranchSum(root,runningSum,sums)
    return sums
def calculateBranchSum(node,runningSum,sums):
	
##if node.left or node.right is None (node has 1 child value)
	if node is None:
		return None
	##initialize the sum from ROOT node!
	newRunningSum = runningSum + node.value
	##if we are at leaf node, add to running sum (if current Node has no children nodes)
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
	else:	
		##cont traversing thru right and left nodes!
		calculateBranchSum(node.left, newRunningSum, sums)
		calculateBranchSum(node.right, newRunningSum, sums)
	
