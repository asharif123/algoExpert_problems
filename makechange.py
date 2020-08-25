def numberOfWaysToMakeChange(n, denoms):
	#n target amount, denoms -> denominations
    # create indices for amount n entered from 0 to n (target amount)
	# every value that we store in indices min number of ways to make change
	# at 0 index, start at 1 b/c only 1 way to make 0 dollars, rest are initialized at 0
	# iterate thru each denom and go thru 1 to n
	#ex: 10, [1,5,10,25]
	# compare iff 1 <= 1 (n <= denom) (ways[1] += ways[1-1] ) b/c use initial base case)
	# ways[2] += ways[2-1] -> 0+1 = 1, 0-10 all have 1s since only 1 WAY to make 1s using 0 > n
    # 5, how many denominations can be used to make $1
	#summary: how many denom from array can be used to make change (denom <= change)
	#ways[5] += ways[5-5] -> 2 ways (5 1 dollar bills OR 1 5 dollar bill)
	#if denom <= amount -> ways[amount] += ways[amount-denom]
	#for 5 denomination, ways[5 -> 9] ALL display 1 way, ways[10] = ways[10] + ways[5] = 2+1 = 3
	#10, ways[10] = ways[10] + ways[0] = 3+1 => 4
	#skip 25 b/c greater than ALL amounts
	#space: O(N) (N is target amount)
	#time: O(nd) (d is number of denominatons, and iterating thru each denominations)
	
	##initialize 0 from 0 thru n
	ways = [0 for amount in range(n+1)]
	ways[0] = 1
	for denom in denoms:
	##skip 0 since initialized to 1
		for amount in range(1, n+1):
			if denom <= amount:
				ways[amount] += ways[amount-denom]
	return ways[-1]
	
