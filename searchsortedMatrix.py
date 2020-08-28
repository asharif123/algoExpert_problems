def searchInSortedMatrix(matrix, target):
    # each row is sorted and each column is sorted
	# compare if each number is more or less than target
	#go row by row and start at top right number
	#if target < top right number, value could be to the left of top value and eliminate entire column
	#eelif target > top right number, look at last column only!
	#look at second to last value, if value is less than target, eliminate values to left of it (top row) and look at values below second to last value
	#look at second value in second to last col, if smaller, eliminate to left and value on top
	#compare next value eliminate values to left and top IF value is less than target
	#compare next value, if value is bigger than target, eliminate that value and value below it and move to the left
	#return indices of target value or [-1,-1] if target NOT there
	#space: O(1), time: O(N+M) where N is length length of rows and M is length of cols 
	
	##start at top right corner
	row = 0
	col = len(matrix[0]) - 1
	
	##traverse thru matrix
	##if row goes past len(matrix), we are too far down and if col is -, we are too far left
	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			##eliminate values that are greater than target (numbers below it)
			col -= 1
		
		elif matrix[row][col] < target:
			##eliminate values to left and move down row
			row += 1
			
		elif matrix[row][col] == target:
			return [row,col]
		
	return [-1,-1]
			
