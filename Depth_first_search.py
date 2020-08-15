#DFS goes branch by branch (leftmost to rightmost) and iterates via each node
#BFS explores level by level
#add Node to final array and every child node that node has, call DFS and pass final array
##start with first child node and call DFS then go thru other child nodes
##call DFS on each child node one by one
##we have vertices and edges that connect each individual node
##Time: O(V+E) (V = vertices, E = edges b/c we traverse every vertex and edge to access children nodes using for loop)
##Space: O(V) (storing array holding V diff nodes as we go deeper, add frames to call stack)
class Node:
    def __init__(self, name):
		#name of ROOT node that we are calling
        self.name = name
		#children of node
		self.children = []
##add every child to array
    def addChild(self, name):
		##append new Node to children array
        self.children.append(Node(name))
        
##array has all node names
##
    def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
##Ex: B is child of A so call B.depthFirstSearch(['A']) and add B child to array
##call depthfirstSearch on child and add RECURSIVELY to array
			child.depthFirstSearch(array)
		return array

        
