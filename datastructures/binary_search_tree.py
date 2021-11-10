

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



def main():
	test = BST()
	node1 = Node(55)
	node2 = Node(10)
	node3 = Node(23)
	node4 = Node(56)

	test.insert(node1)
	test.insert(node2)
	test.insert(node3)
	test.insert(node4)



	test.print_tree()

	print(str(test.exists(200)))


if __name__ == "__main__":
	main()
		
			