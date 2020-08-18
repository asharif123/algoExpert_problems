def riverSizes(matrix):
    # treat every element as node in graph
	# if node has 1, must be river and apply 
	# treat as each node and has neighboring nodes
	#keep track of all ones we see and corr rivers (using graph )
	# apply BFS or DFS for each neigboiring 1, STOP when you encounter 0
	##mark node as visited once we have touched upon it!
	# if we encounter node already visited, mark as visited && skip it!!
	# skip anything having zeroes!
	# initialize length = 1 and increase size each time we hit 1
    # once we finish iterating each river, add size to final array
	# time: O(w*h) (w is length and h is height) -> O(N) total number of nodes
	# space: O(w*h) (hold booleans on whether node is/not visited)

	##sizes return the size of EVERY river (having 1 or adjacent 1s)
	sizes = []
	##initialize aux matrix (same size as input matrix having boolean whether or not has been visited)
	visited = [[False for value in row] for row in matrix]
	
	##iterate every matrix by every node
	for i in range(len(matrix)):

	##matrix may NOT have same length and height so iterate via specific length
		for j in range(len(matrix[i])):
			traverseNode(i,j,matrix,visited,sizes)
	return sizes
	
def traverseNode(i,j,matrix,visited,sizes):
		##initialize river size, if you hit 0, stays at 0, else increase by 1
	currentRiverSize = 0
		
	##UNVISITED nodes we need to explore
	nodesToExplore = [[i,j]]
	##whilte we stil have nodes to explore using DFS
	while len(nodesToExplore):
			##pop out node we are exploring
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
			##skip if we visited land
		if matrix[i][j] == 0:
			continue
			##else if we encounter 1 (river)
		currentRiverSize += 1
##find every unvisited neighbor
		unvisitedNeighbors = getUnVisitedNeighbors(i,j,matrix,visited)
		for neighbor in unvisitedNeighbors:
			nodesToExplore.append(neighbor)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)
		
##get ALL unvisited neighbors	
def getUnVisitedNeighbors(i,j,matrix,visited):

	##each node can have UP TO 4 unvisited nodes
	unVisitedNeighbors = []
	##check neighbor above us has been visited or not (NOT on top row)
	
	if i > 0 and not visited[i-1][j]:
		unVisitedNeighbors.append([i-1,j])
	##NOT on bottom row and NOT visited
	
	if i < len(matrix)-1 and not visited[i+1][j]:
		unVisitedNeighbors.append([i+1,j])
	
	##if were NOT on left row and NOT visited
	if j > 0 and not visited[i][j-1]:
		unVisitedNeighbors.append([i,j-1])
		
	##note we add 0 b/c to ensure possibility that length != width of matrix
	##if j is NOT rightmost
	if j < len(matrix[0])-1 and not visited[i][j+1]:
		unVisitedNeighbors.append([i,j+1])
	
	return unVisitedNeighbors
	
			
		 
