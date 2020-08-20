def longestPeak(array):
	#assume there will be at least one peak
    # peak: 3 or more consecutive integers that are increasing and decrease after the peak
	#if cond above is met, stop when you hit larger value
	#doing array iteration approach would require keeping track of ALL peaks
	
	#find all peaks and find longest peak by comparing their lengths
	#peak goes up initially then decreases (tip touching highest value)
	#start iterating at second value b/c CANNOT have peak value at beginning or end of array and
	#compare previous to next adjacent values to determine if we find tip of peak
	#tip of peak occurs when we find value that is greater than BOTH before and after that value! that is
	#the peak
	#O(N) time b/c have to traverse entire length of array
	#b/c we're separating both tip and length of peak, once we find tip, calculate 1st length and
	#store in array, then compare subsequent peak lengths and determine if larger than stored length
	#if yes replace the stored peak w/ new, so O(1) space
	#start at EACH peak value and keep going until we are no longer STRICTLY decreasing from left OR right
    
	##used to keep track of longestPeakLength
	longestPeakLength = 0
	
	#peak values DO NOT occur at beginnin or end of array!
	
	i = 1
	while i < len(array) - 1:
		##find tip of peaks and compute peak lengths
		isPeak = array[i-1] < array[i] and array[i] > array[i+1]
		if not isPeak:
			i += 1
		
		##if peak is found, find ALL strictly decreasing values before and after peak value and compute its length
		else:
			
			##since we know i - 1 is less than current value, compare i - 2 to see if less than i - 1
			leftIdx = i - 2

			##do same for right and left sides to see if STRICTLY decreasing
			while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
				leftIdx -= 1
			rightIdx = i + 2
			while rightIdx < len(array) and array[rightIdx] < array[rightIdx-1]:
				rightIdx += 1

			##compute length of current peak
			currentPeakLength = rightIdx - leftIdx - 1
			
			##compare current peak length to see if it's longer than prev peak length
			longestPeakLength = max(currentPeakLength,longestPeakLength)

			#continue exploring values further to right
			i = rightIdx
	return longestPeakLength
		
