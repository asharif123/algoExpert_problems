def isValidSubsequence(array, sequence):
    # Write your code here.
	# Time Complexity: O(N), Space: O(1)
	sequence_idx = 0
	array_idx = 0
	while (array_idx < len(array) and sequence_idx < len(sequence)):
		if (array[array_idx] == sequence[sequence_idx]):
			array_idx += 1
			sequence_idx += 1
		else:
			array_idx += 1
	if (sequence_idx == len(sequence)):
		return True
	else:
		return False

	

