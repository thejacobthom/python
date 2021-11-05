# index starts at position 0










#First we will create a node, the valuetype that will serve as the building block for our doubly linked list

class Node:

	#here we create an init function for inception of a node. This includes a previous pointer and a next pointer
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None
		
	#here we create a representation function for displaying the node if called upon
	def __repr__(self):
		return self.value


class int_doubly_linked_list:
	
	#another init for the head of the list. This includes a counter for elements in the list and a tail pointer for finding the end quickly
	def __init__(self):
		self.head = None
		self.tail = None
		self.element_count = 0

	#here we have a representation function for displaying the linked list itself, it works by traversing the list and storing the value of each node in an array
	#and then joining the array together separated by arrows ( -> )
	def __repr__(self):
		cur = self.head
		nodes = []

		while cur != None:
			nodes.append(str(cur.value))
			cur = cur.next

		nodes.append("None")

		return " -> ".join(nodes)


	def give_head(self):
		return self.head

	def give_tail(self):
		return self.tail

	#returns the length of the list
	def give_length(self):
		return self.element_count

	#insert the node at the head of the linked list
	def insert_head(self, new_node):
		
		if new_node != None:
			self.element_count+=1
			if self.head == None: #if no head exists
				#set the head and tail to be the new node
				self.head = new_node
				self.tail = new_node

			else: #if there is a current head
				#point the new head's next to be the current head
				new_node.next = self.head
				#point the current head's previous to be the new head
				self.head.prev = new_node
				#reassign the list's head pointer to be the new head
				self.head = new_node

	#insert the node at the tail of the linked list
	def insert_tail(self, new_node):
		if new_node != None:
			self.element_count+=1
			if self.tail == None: #if not tails exists
				#set the head and tail to be the new node
				self.head = new_node
				self.tail = new_node

			else: #if there is a current tail
				#point the new tail's previous to be the current tail
				new_node.prev = self.tail
				#point the current tail's next to be the new tail
				self.tail.next = new_node
				#reassign the list's tail pointer to be the new tail
				self.tail = new_node

	#delete the head of the linked list
	def delete_head(self):
		if self.head != None: #if the head exists
			self.element_count-=1
			if self.head.next != None: #if there is a node after the head
				#set the next nodes prev pointer to be None (remove it's reference to the node (head) before it)
				self.head.next.prev = None
				#create a holder pointer for the current head
				temp = self.head
				#reassign the head pointer to be the next node
				self.head = self.head.next
				#remove the pointer from the previous head to the new head to ensure references are removed
				temp.next = None
			else: #there is no node after the head
				#only element in the list so we remove it
				self.head = None
				self.tail = None

	#delete the tail of the linked list
	def delete_tail(self):
		self.element_count-=1
		if self.tail != None:
			if self.tail.prev != None: # if there is a node before the tail:
				#set the node previous to the tail's previous pointer to be none (remove it's reference to the current tail)
				self.tail.prev.next = None
				#create a temporary pointer for the current tail
				temp = self.tail
				#set the list tail pointer to be the new tail
				self.tail = self.tail.prev
				#remove the previous reference to the new tail from the old tail
				temp.prev = None
			else: #there is is no node before the tail
				#only element in list so we remove it
				self.tail = None
				self.head = None

	#insert the node at position x from the head. if the value goes past the tail, insert at the tail
	def insert_at_distance_from_head(self, distance_from_head, new_node):
		if new_node != None:
			#if no distance, insert new head
			if distance_from_head == 0:
				self.insert_head(new_node)
			else:
				#set a pointer to track location in the list
				cur = self.head
				
				#move down x spaces from the head
				while distance_from_head > 0 and cur.next != None:
					cur = cur.next
					distance_from_head-=1

				#if at the end of list
				if distance_from_head > 0:
					self.insert_tail(new_node)
				else: #if distance count finished
					#insert from prev side
					cur.prev.next = new_node
					new_node.prev = cur.prev

					#insert from cur side
					cur.prev = new_node
					new_node.next = cur

					self.element_count+=1

	#inser the node at positino x from the tail. if the value goes past the head, insert at the head
	def insert_at_distance_from_tail(self, distance_from_tail, new_node):
		if new_node != None:
			#if no distance, insert new tail
			if distance_from_tail == 0:
				self.insert_tail(new_node)
			else:
				#set a pointer to track location in the list
				cur = self.tail

			#move x spaces up from the tail
				while distance_from_tail > 0 and cur.prev != None:
					cur = cur.prev
					distance_from_tail-=1

				#if at the beginning of the lsit
				if distance_from_tail > 0:
					self.insert_head(new_node)

				else: #if distance count finished
					#insert from next side
					new_node.next = cur.next
					cur.next.prev = new_node

					#insert from cur side
					new_node.prev = cur
					cur.next = new_node

					self.element_count+=1

	#insert the node after the first node containing x value from the head. if no value exists, do not insert
	def insert_after_value(self, target_value, new_node):
		if new_node != None:
			cur = self.head
			placed = False

			while cur != None and placed == False: #while not placed and not at the end of the list
				if cur.value == target_value: #if target value
					#Check if tail
					if cur.next == None:
						self.insert_tail(new_node)
					else:
						#insert at next side
						cur.next.prev = new_node
						new_node.next = cur.next

						#insert at cur side
						cur.next = new_node
						new_node.prev = cur

						self.element_count+=1

					#escape loop
					placed = True
				else: #else proceed down the list
					cur = cur.next

	#insert the node before the first node containing x value from the head
	def insert_before_value(self, target_value, new_node):
		if new_node != None:
			
			cur = self.head
			placed = False

			while cur != None and placed == False: # while not placed and not at the end of the list
				if cur.value == target_value:
					#check if head
					if cur.prev == None:
						self.insert_head(new_node)
					else:

						#insert at prev side
						cur.prev.next = new_node
						new_node.prev = cur.prev

						#insert at cur side
						cur.prev = new_node
						new_node.next = cur

						self.element_count+=1
					placed = True
				else: #keep proceeding down the list
					cur = cur.next

	#return the node stored at x position. if no node exists return None
	def node_at_position(self, position):
		cur = self.head

		#while not at the end of the list or at the target position
		while position > 0 and cur != None:
			cur = cur.next
			position-=1

		#if none, return none
		if cur == None:
			return None
		else: #we must be at the target position, return cur
			return cur

	#returns an array with the positions containing the searched for value. Empty array if none found
	def positions_with_value(self, target_value):
		nodes = []
		cur = self.head
		position = 0

		while cur != None: #while not at the end of the list
			if cur.value == target_value: #if target value found
				nodes.append(position) #append location to the array
			position+=1 #increase position count
			cur = cur.next #advance position in the list

		return nodes

	#inserts a node into the list in order with head being the smallest and and tail being the largest
	def insert_in_order(self, new_node):
		if new_node != None:
			cur = self.head
			placed = False
			
			if self.element_count == 0 or self.head.value >= new_node.value: #if a new list or lessthan/equal to head
				self.insert_head(new_node)

			else: #if not a new list

				cur = self.head
				found_spot = False

				while found_spot == False:
					if cur == None: #reached end of list
						found_spot = True

					elif cur.value < new_node.value: #keep going, we want the node that is LARGER than our new node
						cur = cur.next
					else: #the current node is larger than our new node
						found_spot = True

				if cur == None:
					self.insert_tail(new_node)
				else:
					#insert node inbetween nodes
					#fix prev
					cur.prev.next = new_node
					new_node.prev = cur.prev

					#fix next
					new_node.next = cur
					cur.prev = new_node
					self.element_count+=1
				
	#joins two sorted lists in order. they must be sorted BEFORE this function is called
	#possible issue with assigning head
	def join_sorted_lists_in_order(self, listB):
		self.element_count+= listB.give_length()

		curA = self.head
		curB = listB.head
		tailB = listB.tail

		#find new head
		if curA.value < curB.value:
			temp = curA
			curA = curA.next
		else:
			temp = curB
			curB = curB.next

		#save new head, we will use the other as a scrolling pointer for the tail
		temp_head = temp
		while curA != None and curB != None:
			#find which value is less than the other
			if curA.value < curB.value:
				#fix attachment to temporary list
				temp.next = curA
				curA.prev = temp

				#move curA forwards
				curA = curA.next
			else:
				#fix attachment to temporary list
				temp.next = curB
				curB.prev = temp

				#move curB forwards
				curB = curB.next
			
			temp = temp.next

		
		#not finished yet, account for the end of whichever list is left
		if curA != None: #if listA is left
			temp.next = curA
			curA.prev = temp
			#tail is already set
		else: #listB must be left
			temp.next = curB
			curB.prev = temp
			self.tail = tailB #reassign tail pointer

		self.head = temp_head

	#joins list B to the end of the current list
	def join_list(self, listB):
		temph = listB.give_head()
		tempt = listB.give_tail()
		length = listB.give_length()
		
		if temph != None:
			temph.prev = self.tail
			self.tail.next = temph
			self.element_count+=length
			self.tail = tempt

	#returns True if node with value x exists, else returns False
	def exists(self, target_value):
		arr = self.positions_with_value(target_value)
		if len(arr) == 0:
			return False
		else:
			return True

	#sorts the list by using the inser_in_order() function. This makes it an insertion sort algorithm
	def sort(self):
		listS = int_doubly_linked_list() # define a new list

		cur = self.head #set the current pointer
		while cur != None:
			temp = cur #assign the current pointer to place holder
			cur =  cur.next #progress forwards to the nex elemetn of the list

			temp.next = None #detach the current node's next
			temp.prev = None #detach the current node's prev

			listS.insert_in_order(temp) #insert the node into the new list

		self.head = listS.head #assign the new list's head as the head of the list
		self.tail = listS.tail #assign the new lists's tail as the tail of the list

	#deletes node at given position if one exists
	def delete_position(self, target_position):
		if target_position <= self.element_count:
			pos = 0
			cur = self.head

			# if head, reassign
			if target_position == 0:
				self.head = cur.next

			#if tail, reassign
			if target_position >= self.element_count-1:
				self.tail = cur.next

			#while not at target
			while pos != target_position and cur != None:
				cur = cur.next #push position forwards
				pos+=1 #increment position counter

			if cur != None:
				self.element_count-=1

				#if previous, patch it up
				if cur.prev != None:
					cur.prev.next = cur.next
				else: #must be the head so we have a new head
					self.head = cur.next

				#if next, patch it up
				if cur.next != None:
					cur.next.prev = cur.prev
				else: #must be the tail so we have a new tail
					self.tail = cur.prev

	#deletes the first node with the target value
	def delete_node_with_value(self, target_value):
		pos = 0
		cur = self.head
		deleted = False

		#while not at target
		while cur != None and deleted != True:

			if cur.value == target_value:

				self.element_count-=1
				deleted = True

				#if previous, patch it up
				if cur.prev != None:
					cur.prev.next = cur.next
				else: #must be the head so we have a new head
					self.head = cur.next

				#if next, patch it up
				if cur.next != None:
					cur.next.prev = cur.prev
				else: #must be the tail so we have a new tail
					self.tail = cur.prev



			cur = cur.next #push position forwards

	def delete_all_with_value(self, target_value):
		pos = 0
		cur = self.head

		#while not at target
		while cur != None:

			if cur.value == target_value:

				temp = cur.next

				self.element_count-=1

				#if previous, patch it up
				if cur.prev != None:
					cur.prev.next = cur.next
				else: #must be the head so we have a new head
					self.head = cur.next

				#if next, patch it up
				if cur.next != None:
					cur.next.prev = cur.prev
				else: #must be the tail so we have a new tail
					self.tail = cur.prev

				cur = temp
			else:
				cur = cur.next #push position forwards
	

	#return the head of the list and then delete it
	def pop(self):
		holder = self.give_head()
		self.delete_head()
		return holder

listA = int_doubly_linked_list()
listB = int_doubly_linked_list()
listC = int_doubly_linked_list()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node33 = Node(3)
node4 = Node(4)
node44 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node8 = Node(8)
node9 = Node(9)
node99 = Node(9)
node10 = Node(10)
node11 = Node(11)

listA.insert_tail(node1)
print(listA)
listA.insert_tail(node3)
print(listA)
listA.insert_at_distance_from_head(2, node4)
print(listA)
listA.insert_head(node33)
print(listA)
print("-- done making listA --")

listB.insert_tail(node6)
print(listB)
listB.insert_in_order(node2)
print(listB)
listB.insert_in_order(node7)
print(listB)
listB.insert_in_order(node5)
print(listB)
print("-- done making listB --")

listC.insert_in_order(node8)
print(listC)
listC.insert_before_value(8, node9)
print(listC)
listC.insert_after_value(9, node10)
print(listC)
listC.insert_tail(node44)
print(listC)
listC.insert_at_distance_from_tail(1, node99)
print(listC)
listC.insert_head(node11)
print(listC)
print("-- done making listC --")


print("head of list's A, B, and C in order: {} {} {}".format(listA.give_head().value, listB.give_head().value, listC.give_head().value))
print("tails of list's A, B, and C in order: {} {} {}".format(listA.give_tail().value, listB.give_tail().value, listC.give_tail().value))
print("lengths of list's A, B, and C in order: {} {} {}".format(listA.element_count, listB.element_count, listC.element_count))

print("-- joining lists A and B --")
listA.join_list(listB)
print(listA)

print("-- sorting list A -- ")
listA.sort()
print(listA)
print("of list A - head, tail, length: {} {} {}".format(listA.give_head().value, listA.give_tail().value, listA.element_count))

print("-- sorting list C --")
listC.sort()
print(listC)

print("big test {}".format(listA.node_at_position(4).next.value))








print(" -- sorted joining list A and C -- ")
listA.join_sorted_lists_in_order(listC)

print(listA)
print("positions with value 3: {}".format(listA.positions_with_value(3)))
print("positions with value 4: {}".format(listA.positions_with_value(4)))
print("positions with value 7: {}".format(listA.positions_with_value(7)))

print("does 8 exist?: {}".format(listA.exists(8)))
print("does 20 exist?: {} ".format(listA.exists(20)))

print("what value is at position 2?: {}".format(listA.node_at_position(2).value))
print("what value is at position 8?: {}".format(listA.node_at_position(8).value))

print("pop from list A: {}".format(listA.pop().value))
print("pop from list A: {}".format(listA.pop().value))
print("pop from list A: {}".format(listA.pop().value))
print(listA)

print("-- deleting node at position 9 --")
print("-- deleting node at position 3 --")
listA.delete_position(9)
listA.delete_position(3)
print(listA)


print("deleting first instance of 4")
listA.delete_node_with_value(4)
print(listA)

print("deleting all instances of 9")
listA.delete_all_with_value(9)
print(listA)