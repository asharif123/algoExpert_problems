def zigzagTraverse(array):
    # can either go down or up (straight or diagonally)
	# start at top left corner AND go down initially by 1
	# to go up diagonally, move up col by 1 and row to right by 1
	# to go down diagonally, move left of row by 1 and down col by 1
	# only at perimeter do we either go down or up or right by 1 when we FIRST hit value along perimeter
	# when we start or hit value at col 0, we go down by 1 but if we hit bottom left, move right by 1
	# AND then go diagonally up
	#ex [[1,3,4,10],
		#[2,5,9,11],
	##	 [6,8,12,15],
	##	 [7,13,14,16]]
		 
	# if we hit value at top row, move to right by 1 (last column) and go diagonally left to first col BUT
	# if we hit value at bottom left of first col, go down by 1 and diagonally up until we hit value at top row
	# if we hit top right node, go down by 1 and move diagonally down to value at bottom row
	# if we hit value at bottom row, move to the right by 1 and then move diagonally by 1
	# end algo when we hit last value in array AND can't access anymore values (out of bound)
	## update direction EACH time we hit any value in the perimeter bounds AND move by 1
	## Time: O(N) and space: O(N)
	
    ##see if were at perimeter or inside the 2D array from there determine how to traverse
	##see if were at first row/col or first/last col
	
	height = len(array)-1
	
	##NOTE: may NOT be square matrix so need to use array[0]
	width = len(array[0])-1
	
	##store all values that we traverse in array
	results = []
	
	##track our position by row and col, start at top left corner
	row,col = 0,0
	
	##start by going down (since we INITIALLY go down from top left corner)
	goingDown = True
	
 	##while loop to ensure we are NOT out of bounds (inside 2D array)
	##algo ends when we are out of bounds from hitting bottom right value
	
	while not isOutOfBounds(row,col,height,width):
		
		##add starting value to results array
		results.append(array[row][col])
		
		##see what direction were going (either down or up straight/diag)
		
		##check on if we're going down
		if goingDown:
		
		##if we're goingDown already AND if at leftmost column or final row, we will NOT be goingDown
			if col == 0 or row == height:
				goingDown = False
				
				##if we are at botton of matrix, move col to right by 1
				if row == height:
				
					col += 1
				
				##if we are NOT at bottom of matrix
				else:
					row += 1
					
			##if we are going down and NOT at first col or last row, go diagonally up
			else:
				row += 1
				col -= 1
				
		##if were NOT going down
		else:
			##check if were going down
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row += 1
			##if col != width, first row move right y 1
				else:
					col += 1
			
			##go diagonally down
			else:
				row -= 1
				col += 1
			
			
	return results
##define our outofbounds function to determine IF we are out of bounds
def isOutOfBounds(row,col,height,width):
	return row < 0 or row > height or col < 0 or col > width
	
	
	
	
