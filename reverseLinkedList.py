def reverseLinkedList(head):
   #                                p1   p2
    # reverse linked list (ex: 0 -> 1 -> 2 -> 3 -> 4 -> 5)
	# each node has value property and .next that points to next
	# best way to solve: put aside all edge cases and change pointer of 1 node in list and buid from there
	# ex: select middle value 2, have P point at 2, to reverse node 2, grab .next and point to 1 NOT 3!
	# at 2, do not have access to 1 node! (p2 points at 2 and p1 points at prev value 1 )
    # p2.next = p1 (ex: 0 -> 1 ->  2  3 -> 4 -> 5) (point to node before it) dont have access to 1 node
	#                          <-
	# p1 points to 1 (p2.next = p1) (want to reverse 3 node which has been lost)
	# if we call p2.next = p1 BEFORE giving reference to 3,  p2.next is lost
	# so we need p3 node
	#           p1   p2   p3
	# (ex: 0 -> 1 -> 2 -> 3 -> 4 -> 5)
	#                    p1   p2   p3
	# p2.next = p1 (0 -> 1 ->  2  3 -> 4 -> 5) (point to node before it) dont have access to 1 node
	#                          <-
	# now move on to p3 where we have pointer point to 2 but need access to 4 and access to 2 SO shift p1,p2,p3 to right
	# 3 nodes are required to update each node 
	# p2.next = p1 (0 -> 1 ->  2 3   4 -> 5) (point to node before it) dont have access to 1 node
	#					   <- 
	#need to update p1 = p2 and if NOT done, when we make p2 == p3, p2 will be lost and p1 will lost connection
	#p1 = p2, p2 = p3, p3 = p3.next
	
	##ALGO Summary:
	##reverse the head .next property (p2 == currentNode) (as long as p2 is not none, )
	##p3 = p2.next (p3 defines third pointer)
	##p2.next = p1
	##increment:
	##p1 = p2, p2 = p3
	##p1 p2   p3
	##   0 -> 1 -> 2 -> 3 -> 4 -> 5 (start at head)
	## Time: O(n), Space: O(1)
	
	##declare our pointers
	prevNode = None
	
	#we want currentNode.next property to be updated
	currentNode = head
	
	#keep going as long currentNode is NOT none
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = prevNode
		prevNode = currentNode
		currentNode = nextNode
	return prevNode ##it's final NON-null value in linked list while nextNode and currentNodes are null
	
