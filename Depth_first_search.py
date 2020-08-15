# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
#Grab all nodes, put them in array and return it
# and methods to the class.
#queue -> FIFO (first added ot queue is first out)
# start at root node and add it to queue
#add A node to queue and on top of queue declare currentNode
#grab pop from queue add it to current, add to final array add all child nodes of A to queue 
#add name to final array and add all child nodes of A to queue 
#Time: O(V+E), Space: O(V)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		#hold the first node (ROOT), self is node we are caalling BFS on
        queue = [self]
		while queue:
			currentNode = queue.pop(0)
			array.append(currentNode.name)
		##add every child of popped node to the queue (ex: if popping 'B', add 'E' and 'F')
			for children in currentNode.children:
				queue.append(children)
        return array
