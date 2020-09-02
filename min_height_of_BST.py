def minHeightBst(array):
##create function of binary search tree and return root ad minimize height of BST
##height of BST, depth of deepest node (minimize that!)
##ex: [1,2,5,7,10,13,14,15,22] ##when question has special properties (such as being sorted and unique values)
##height: length of longest branch (minimize length of both sides of BST b/c longst side IS height)
##be as balanaced as possible (same number nodes in left as right subtree)
##BST property: every node to left must be smaller than its ancestor and right must be larger  
##sorted array tells us which are smaller and larger than other values
#Ex: 
##10
##/\
#2  14
#/\ /\
#1 513 15 
#  \    \
#  7     22
# if we iterated each value in this array [1,2,5,7,10,13,14,15,22] it would result in adding each value below one another AND
# result in LARGEST height
##so make middle value as root, values of left put left part of subtree, and right values put on right subtree
##distainct integers are impt b/c if duplicate, no guarantee values would go to left or right
#[1,2,5,7,10,13,14,15,22] middle element is 10 make it root node (create left and right subtree)
#left is middle of left (pick 2 but you can pick 5), then pick mid of 5 and 7 (5 and 7 both go to right) and 1 to left
#right subtree: middle node either 14 or 15 (picking 14)
##summary: keep picking middle elements in our array or right/left subarrays
##space: O(N) b/c storing N nodes in memory
##time: O(Nlog(N)) b/c inserting N noodes in binary and inserting node takes log(N) time
##alt: time: O(N) inserting N nodes

##first approach: inserting every value in array and take middle value of each subarray and insert
##need recursive element that takes array,BST,start and ending indices of subarray we are looking at to grab middle value of each subarray
##
	##initially, NO BST has been created (needs to be created from insert function!!)
	return constructMinHeightBst(array,None,0,len(array)-1)

def constructMinHeightBst(array,bst,startIdx,endIdx):
 
	##base case when we run out of values (endIdx < startIdx)
	if endIdx < startIdx:
		return None
		
	##calculate middle index, round down, may NOT be divisible by 2
	midIdx = (startIdx + endIdx) // 2
	
	##grab value we want and add to BST
	valueToAdd = array[midIdx]
	
	##create root node IFF bst is none
	if bst is None:
		bst = BST(valueToAdd)
		
	##else if we HAVE bst, just apply insert method
	else:
		bst.insert(valueToAdd)
	
	##call recursively on other subarrays gooing from left subarray
	constructMinHeightBst(array,bst,startIdx,midIdx-1)
	
	##call recursively on other subarrays gooing from right subarray
	constructMinHeightBst(array,bst,midIdx+1,endIdx)
	
	##return final bst containing ALL inserted values
	return bst
		
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
