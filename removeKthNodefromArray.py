# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
		# Write your code here.
		#CANNOT traaverse single linked list backwards
		#use 2 pointers: first and second, have both point to head value
		#have second traverse BEFORE first and go up to k nodes
		#move both same pace until second goes past tail of linked list (which points to null, second -> None)
		#grab pointer for value before node to remove and point it to .next.next
		#keep track of node BEOFRE node to remove
		#to remove head node, second will be pointing to null so you can just remoe head 
		#since counter starts at 1, once you reach counter, have it point to n nodes ahead of main node 
		#you want to be K nodes AHEAD of first so that's why you include k
		
	first = head
	second = head
	for i in range(k):
		second = second.next
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		##if you reach case where you're removing HEAD node ONLY, you can just return
	else:
		while second.next:
			second = second.next
			first = first.next
		first.next = first.next.next
	return 
