

#first we need a class for the nodes

class Node:

	#an init sequence for the first call
	def __init__(self, value):

		#save that value
		self.value = value
		#and then two pointers for it's children
		self.childL = None
		self.childR = None

	def __repr__(self):
		return str(self.value)

class BST:

	def __init__(self, root = None):

		self.root = root

		#to keep track of how tall the tree is, may be useful when displaying it
		self.height = 0

	def __repr__(self):
		self.print_tree

	# this function inserts a node into the array using recursion, parent is automatically set to none 
	# on first call and then used to determine place in the tree as the function progresses
	def insert(self, node, parent = None):
		
		#if new tree
		if self.root == None:
			#this new node is now the root
			self.root = node

		
		else:
			#else check if this is first call
			if parent == None:
			#if first call, assign parent to root
				parent = self.root

			#find out where the node should go
			if node.value < parent.value:
				#if it goes to the left, does it have a new node to branch from?
				if parent.childL != None:
					#if it does, call insert on that node
					self.insert(node, parent.childL)
				else:
					#if it doesn't, insert the node here!
					parent.childL = node

			#rinse and repeat for the right side...
			if node.value >= parent.value:
				#if it goes to the left, does it have a new node to branch from?
				if parent.childR != None:
					#if it does, call insert on that node
					self.insert(node, parent.childR)
				else:
					#if it doesn't, insert the node here!
					parent.childR = node

	def print_tree(self, height = 0, parent = None):
		#check if tree even exists
		if self.root == None:
			print("This tree is empty")
		else:
			#if no parent, we are at the start of the tree
			if parent  == None:
				#assign parent to root
				parent = self.root

			#print the current node
			print("\t"*height + str(parent.value))

			#if node has a left child
			if parent.childL != None:
				print("\t"*(height+1) + "-L-")
				self.print_tree(height + 1, parent = parent.childL)

			if parent.childR != None:
				print("\t"*(height+1) + "-R-")
				self.print_tree(height + 1, parent = parent.childR)


	#returns the node if found, otherwise returns None
	def search(self, target_value, parent = None, check = False):
		#check if tree even exists
		if self.root == None:
			print("This tree is empty")
		else:
			# if first time running and parent is none, return none
			if parent == None and check == False:
				parent = self.root

			#if not first time running and hit none, return none
			elif parent == None and check == True:
				return None

			#if we found the right value, return that node
			if parent.value == target_value:
				return parent

			#target val must be less than current node so we use the left child as the parent
			elif target_value < parent.value:
				return self.search(target_value, parent.childL, check = True)

			#target val must be greater than current node so we use the right child as the parent
			else:
				return self.search(target_value, parent.childR, check = True)


	#a modified version of search that simply returns true if the value exists and false if it does not
	def exists(self, target_value, parent = None, check = False):
		#check if tree even exists
		if self.root == None:
			return False
		else:		
			# if first time running and parent is none, return none
			if parent == None and check == False:
				parent = self.root

			#if not first time running and hit none, return none
			elif parent == None and check == True:
				return False

			#if we found the right value, return that node
			if parent.value == target_value:
				return True

			#target val must be less than current node so we use the left child as the parent
			elif target_value < parent.value:
				return self.exists(target_value, parent.childL, check = True)

			#target val must be greater than current node so we use the right child as the parent
			else:
				return self.exists(target_value, parent.childR, check = True)

	#possible issues, see below
	def delete(self, target_value):
		#check if tree even exists
		if self.root == None:
			print("This tree is empty")
		else:
			# have to start somewhere right?
			current_node = self.root
			#keeps track of parent
			previous_node = None
			#keeps track of where the current node is in relation to its parent. arbitrary naming convention
			last_direction_left = True
			#to keep track if the exeuction is done
			deleted = False

			while current_node != None and deleted == False:

				if current_node.value == target_value:

					deleted = True
					#delete this node

					#check if final root
					if current_node == self.root and current_node.childL == None and current_node.childR == None:
						self.root = None
					else:

						#if any children exist..
						if current_node.childL != None or current_node.childR != None:	

							#if both children exist
							if current_node.childL != None and current_node.childR != None:					
								
								#find the leftmost node of the right child
								#save the current working parent (default is just the right node)
								new_parent = current_node.childR

								new_parent_previous = None
								#keep going left until cannot go left any longer
								while new_parent.childL != None:
									#save the parent
									new_parent_previous = new_parent
									#advance the new parent down the tree
									new_parent = new_parent.childL


								#adjust the pointer for the parent and set new pointers for the new node
								if new_parent_previous != None:
									new_parent_previous.childL = new_parent.childR 

									new_parent.childL = current_node.childL
									new_parent.childR = current_node.childR

								else:
									#if no previous parent just shift the left child up
									new_parent.childL = current_node.childL

								
							#else if only has left children
							elif current_node.childL != None:

								#assign new parent, no reassignment need for its pointers, only its parent which is handled below
								new_parent = current_node.childL

							#else if only has right children
							elif current_node.childR != None:

								new_parent = current_node.childR

							#if had a previous node
							if previous_node != None:
								if last_direction_left == True:
									#set the left pointer to the new parentb
									previous_node.childL = new_parent
								else:
									#set the right pointer to the new parent
									previous_node.childR = new_parent

							#else must be the root
							else: 
								self.root = new_parent

						#no children
						else:
							if last_direction_left == True:
								#set the left pointer to None
								previous_node.childL = None
							else:
								#set the right pointer to None
								previous_node.childR = None



				#else we're still searching
				elif target_value < current_node.value:
					#if it's less than, repeat the loop with the new node
					#save the previous node (for it's pointer)
					previous_node = current_node
					#advance the current node
					current_node = current_node.childL
					#change direction keeper
					last_direction_left = True


				else:
					#must be larger than current node
					#save the previous node (for it's pointer)
					previous_node = current_node
					#advance the current node
					current_node = current_node.childR
					#change direction keeper
					last_direction_left = False

	#returns an arrary going (root, left branch, right branch)
	def traverse_preorder(self, cur_node = None, check = False):
		arr = []
		#if node does not exist
		if cur_node == None:

			if check == False:
				#this must be the first run, assign cur to root
				cur_node = self.root
				#set check to true as first run is completed
				check = True
			else: #we've hit the end of a branch
				#return an empty array because python lets us extend by empty arrays
				return arr

		#extend the array by the current node
		arr.extend([cur_node.value])
		#recur and extend on left
		arr.extend(self.traverse_preorder(cur_node.childL, check))
		#recur and extend on right
		arr.extend(self.traverse_preorder(cur_node.childR, check))

		
		return arr

	#returns an arrary going (left branch, root, right branch)
	def traverse_inorder(self, cur_node = None, check = False):
		arr = []
		#if node does not exist
		if cur_node == None:

			if check == False:
				#this must be the first run, assign cur to root
				cur_node = self.root
				#set check to true as first run is completed
				check = True
			else: #we've hit the end of a branch
				#return an empty array because python lets us extend by empty arrays
				return arr

		#recur and extend on left
		arr.extend(self.traverse_inorder(cur_node.childL, check))
		#extend the array by the current node
		arr.extend([cur_node.value])
		#recur and extend on right
		arr.extend(self.traverse_inorder(cur_node.childR, check))

		return arr

	#returns an arrary going (left branch, right branch, root)
	def traverse_postorder(self, cur_node = None, check = False):
		arr = []
		#if node does not exist
		if cur_node == None:

			if check == False:
				#this must be the first run, assign cur to root
				cur_node = self.root
				#set check to true as first run is completed
				check = True
			else: #we've hit the end of a branch
				#return an empty array because python lets us extend by empty arrays
				return arr

		#recur and extend on left
		arr.extend(self.traverse_postorder(cur_node.childL, check))
		#recur and extend on right
		arr.extend(self.traverse_postorder(cur_node.childR, check))
		#extend the array by the current node
		arr.extend([cur_node.value])

		return arr



def main():
	test = BST()
	node1 = Node(50)
	node2 = Node(25)
	node3 = Node(10)
	node4 = Node(30)
	node5 = Node(75)
	node6 = Node(60)
	node7 = Node(59)
	node8 = Node(61)
	node9 = Node(90)
	node10 = Node(91)
	node11 = Node(80)
	node12 = Node(85)

	test.insert(node1)
	test.insert(node2)
	test.insert(node3)
	test.insert(node4)
	test.insert(node5)
	test.insert(node6)
	test.insert(node7)
	test.insert(node8)
	test.insert(node9)
	test.insert(node10)
	test.insert(node11)
	test.insert(node12)



	travtest1 = test.traverse_preorder()
	travtest2 = test.traverse_inorder()
	travtest3 = test.traverse_postorder()

	print("-------- traversals -------")
	print (travtest1)
	print (travtest2)
	print (travtest3)

	print("-------- exists -------")
	print(test.exists(91))
	print(test.exists(85))
	print(test.exists(12412))

	print("-------- search -------")
	print(test.search(75))
	print(test.search(10))
	print(test.search(61))

	print("-------- deletions -------")
	test.delete(8768) #value doesn't exist
	test.delete(test.root.value)
	test.delete(test.root.value)

	test.print_tree()

	test.delete(91)
	test.delete(61)
	test.delete(test.root.value)
	test.delete(test.root.value)
	test.delete(test.root.value)

	test.print_tree()

	test.delete(test.root.value)
	test.delete(test.root.value)
	test.delete(test.root.value)
	test.delete(test.root.value)

	print("-------- final root node -------")
	test.print_tree()

	test.delete(test.root.value)



	test.print_tree()



if __name__ == "__main__":
	main()
		
			