def caesarCipherEncryptor(string, key):
    # Time: O(n), Space: O(n)
	#ex: x -> 120, shift = 4, x+shift => 124 -> b, (98)
	#ex: y -> 121, shift = 5. y+shift => 126 -> d, (100)
	#ex: y -> 121, shift = 52, y+shift => 173 -> y 
	#for letter in string
	#if ord(letter)+shift > ord(z):
	converted_string = ''
	for letter in string:
	#if ord(letter)+shift < ord('z'), convert letter and add to empty string
		if ord(letter)+key <= ord('z'):
			converted_string += chr(ord(letter)+key)
	# if ord(letter)+shift > ord('z'), reroute the result to fall btwn 97 to 122
	#ex: if letter is 'b' and 98+26 (shift) -> 124, should return 'b' (98)
	#modulus 122 is used to ensure we never exceed ord(value) past 122!
	#if we have big shift (ex: shift is 52, using 122 modulus would not allow values to fall in 97 to 122 range)
	#so we need to divide by modulus 26 to compensate for that!
		elif (ord(letter)+key) > ord('z'):
			converted_string += chr(96+((ord(letter)+key)%122)%26)
	return converted_string
			
	
