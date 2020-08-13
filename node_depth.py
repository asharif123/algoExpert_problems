def nodeDepths(root, depth = 0):
		#pass depth to recursive call
		#handle base case
		#if root has no children values, return 0
	if root is None:
		return 0
		
		#increase depth by 1 each time we traverse down tree
		#left and right nodes increase by 1
	return depth + nodeDepths(root.left,depth+1) + nodeDepths(root.right,depth+1)
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
