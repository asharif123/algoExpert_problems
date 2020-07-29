def getNthFib(n):
    first_value = 0
	second_value = 1
	

	if n == 1:
		return first_value
	elif n == 2:
		return second_value
	elif n > 2:
		
		for i in range(2,n):
			total = first_value + second_value
			first_value = second_value
			second_value = total
			
		return total
		
	
		
	
	
   

		
	
	
   
