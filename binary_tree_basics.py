# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
# Binary Tree properties: ALL values of root must be bigger than root on right and all left values must be LESS than root node
#Average: O(log(N)) b/c there are cases when eliminating by half is impossible ex: if you have single branch tree w/o left nodes
#worst: O(N)
#Space: O(log(N)) recursively or O(N) worst case b/c you use previous call stacks (USING RECURSION!)
#OR O(d) space
#if iterative: Space: O(1)
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#Time: Olog(N), Space: O(1)
#Worse Case: O(N), Space: O(1)
    def insert(self, value):
		# call on root and traverse to see where we at
		# currentNode is Node we call insertion method on
		currentNode = self
		
		while currentNode:
			if value < currentNode.value:
				##if left node is actual BST
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self


    def contains(self, value):
		currentNode = self
		#this ensures that we go thru EVERY existing node
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			elif currentNode.value == value:
				return True
		#If we encounter empty node, return False
        return False

#find node that you wanna remove and then actually remove it
#keep track of parentNode b/c to reassign childNodes of parentNode we are removing
#NOTE: root node has NO parent node
    def remove(self, value, parentNode = None):
        currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
			#parentNode becomes currentNode we were just exploring
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
## found the node of value we want to remove
			else:
## dealing node having 2 children nodes
##find smallest value of right subtree, replace value we're removing with that and remove 
##smallest value from right subtree
				if currentNode.left is not None and currentNode.right is not None:
##get the SMALLEST value of right subtree to replace 
					currentNode.value = currentNode.right.getMinValue()
#currentNode.value = smallest value of right subtree and parentNode defaults to currentNode
					currentNode.right.remove(currentNode.value,currentNode)
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						pass
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
		return self
				
	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value
			
			
