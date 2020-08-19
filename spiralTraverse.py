def spiralTraverse(array):

	##[[1,2,3,4],
	##[10,11,12,5],
	##[9,8,7,6]]
	## assume either rectangular or square shape (ask interviewer)
    # starting row -> ending column -> ending row -> starting column (get dimensions of array)
	# traversal of several perimeters (outer and inner perimaters)
	
	# iterate top row: iterate via all columns between starting and ending columns
	# iterate ending column: iterate starting row + 1 to ending row (starting row + 1 to ensure we dont readd last value in first row) 
	# iterating ending row: itertate ending-1 (ensure we don't readd last value) to starting col
	# starting col: iterate ending row -1 to starting row + 1
	# finished traversing outer perimieter, to grab inner perimeter:
	# update SR by 1, SC by 1, decrease eC by 1, decrease eR by 1
	#ed algo when SR <= ER or SC <= EC
	
	# O(N) time b/c traversing every value in matrix, O(N) space b/c stroing all N values
	
	result = []
	
	#get dimensions of value from 2D array
	startRow,endRow = 0,len(array)-1
	startCol,endCol = 0,len(array[0])-1
	
    #return array once starting row > ding row and starting col >ending col
	while startRow <= endRow and startCol <= endCol:
	
		##traverse first row
		for col in range(startCol,endCol+1):
			result.append(array[startRow][col])
			
		##traverse last col, startRow+1 ensure we DO NOT readd same entry
		for row in range(startRow+1,endRow+1):
			result.append(array[row][endCol])
			
		##traverse bottom row
		for col in reversed(range(startCol,endCol)):

			result.append(array[endRow][col])
			
			
		##traverse starting col, start from row above last and end at row below starting
		for row in reversed(range(startRow+1,endRow)):

			result.append(array[row][startCol])
			
		##push bounds inwards to traverse next set of inner perimeters
		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1
	
	return result
