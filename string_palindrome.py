#time: O(n), space O(n)
def isPalindrome(string):
    # Write your code here.
    string_backwards = ''
	for i in range(len(string)-1,-1,-1):
		string_backwards += string[i]
	return string_backwards == string
