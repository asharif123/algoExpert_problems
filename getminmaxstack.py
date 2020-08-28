# Feel free to add new properties and methods to the class.
#ex: stacking books, last book we put on top of table is first to look at (LIFO)
#queue: LILO
class MinMaxStack:
##pekk/pop values and access min/max values in stack
##EX: 5,7,2
##peek -> look at value at top of stack, push all values in stack, empty array
##push 5, 7 and 2 -> [5,7,2] peek at top value (2) using array.pop(), access last value in array
##keep track of min/max values (add vlaue at stack and keep track of min/max, if we pop min/max changes)
##can't keep track of min/max when we pop

##when we push value on top of stack, keep track of  prev values
##so store min/max value at any point in stack [5] using dict (min = 5, max = 5), add 7 (min = 5, max  7)
##store min and max in another empty array and update min/max by looking at latest value added
##so if we pop, max/min can be updated with prev values
##each element in list is 2 values
##O(1) time and space for all of them
    
	def __init__(self):
	##holds min and max values as dict ("min": min, "max": max)
		self.minMaxStack = []
		
	##stack holding all values
		self.stack = []
	
	def peek(self):
        # read last value in array
		return self.stack[-1]
       

    def pop(self):
		#minMaxStack in sync with self.stack 
        # remove value from stack and MinMaxStack b/c value popped from minmaxstack is only releveant to point time in stack where we have value that were now poppping off 
		self.minMaxStack.pop()
		return self.stack.pop()
        

    def push(self, number):
        #update min and max values, if pushing one value, min anx max point to same number
		newMinMax = {"min": number, "max": number}
		
		##if we have values in minMaxStack and have values in stack
		if len(self.minMaxStack):
		##see last value in minmaxStack and compare
			lastMinMax = self.minMaxStack[-1]
			newMinMax["min"] = min(number,lastMinMax["min"])
			newMinMax["max"] = max(number,lastMinMax["max"])
		##add new value to minMaxStack
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)
		
			
			
        pass

    def getMin(self):
        return self.minMaxStack[-1]["min"]
        pass

    def getMax(self):
        return self.minMaxStack[-1]["max"]
        pass
