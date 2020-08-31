def levenshteinDistance(str1, str2):
    # ex: str1 = "Mic"
	# str2 = "Mac"
	# 	"" "M" "i" "c"
	# "" 0  1   2   3
	# "M"1  0   1   2 
	# "a"2  1   1   2
	# "c"3  2   2   1  
	
	
	##str1 = "abc", str2 = "yabd"
	#    "" "a" "b" "c"
	# ""  0  1   2   3
	# "y" 1  1   2   3
	# "a" 2  1   2   3
	# "b" 3  2   1   2
	# "d" 4  3   2   2
	#if empty string, just fill out initial row/col with however long string is
	#if letters are equall, get i -1 and j - 1 diagnol from matrix array
	#else, take min of 3 neighbors and add it to matrix plus 1
	#time and space complexity: O(N*M)
	
	##create 2D matrix:
	matrix = [[0 for j in range(len(str1)+1)] for i in range(len(str2)+1)]
	
	
	##initialize cases where either first or second word is empty
	
	for i in range(len(str2)+1):
		matrix[i][0] = i
		
	for j in range(len(str1)+1):
		matrix[0][j] = j
		
	##iterate thru each row AND each column starting at second row AND col b/c initial row and col have been filled w/ length of str1 AND str2
	# look diag b/c we can cross letters out since they're equal and compare prev letters
	# else take min of 3 neighboring boxes AND add 1 to it! (E[r][c] = 1 + min(E[r][c-1], E[r-1][c], E[r-1][c-1])
	# SINCE we shifted by 1 on BOTH row and col (due to adding empty string, compare r -1 to c - 1) (ex if we compare a to y, both are at 1)
	# so compare if string1[r-1] = string2[c-1] NOT string1[r] = string2[c]
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1)+1):
			if str2[i-1] == str1[j-1]:
				matrix[i][j] = matrix[i-1][j-1]
				
			else:
				matrix[i][j] = 1 + min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])
				
	return matrix[-1][-1]
				
			
				
			
    pass
