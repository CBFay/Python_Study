# linked_list.py
# Growing implementation of a Linked List
# Created on 11.27.2017 by CB Fay
# Updated on 11.30.2017

class node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
	def __str__(self):
		return str(self.data)
		
class linked_list:
	def __init__(self):
		self.root = None # this will change every time we add a new node.
		self.size = 0
	
	# creates a linked_list from a sequential data type
	def __init__(self, sequence): # O(k)
		self.root = None
		self.size = 0
		for i in range(1, len(sequence)+1, 1):
			self.add(sequence[-i])
			
		
	def __len__(self):
		return self.size
		
	def __str__(self):
		list_string = '['
		node = self.root
		while node:
			list_string += repr(node.data)
			node = node.next
			if node:
				list_string += ', '
		list_string += ']'
		return list_string
		
	def __getitem__(self, index):
		if index < 0:
			distance = self.size + index
		else:
			distance = index
		node = self.root
		for i in range(distance):
			node = node.next
		return node.data
		
	def add(self, data):
		new_node = node(data, self.root) # create a new node
		self.root = new_node # set the root node to the one we just added
		self.size += 1
		
	def extend(self, elements):
		for x in elements:
			self.add(x)
	
	# is buggy
	def remove(self, deleteme):
		node = self.root
		if node.data == deleteme:
			self.root = self.root.next
		else:
			while node.next:
				previous = node
				node = node.next
				if node.data == deleteme:
					previous.next = node.next
					self.size -= 1
	
	def remove_duplicates(self): # O(n)
		if self.size < 2:
			return
		inlist = set()
		node = self.root
		if self.size > 1:
			prev = None
			while node:
				if node.data in inlist:
					prev.next = node.next
				else:
					inlist.add(node.data)
					prev = node
				node = node.next

	
	def from_last(self, k):
		if k < 1 or k > self.size:
			return None
		distance = self.size - k
		n = self.root
		for i in range(distance):
			n = n.next
		return n.data
			
	def list_print(self):
		node = self.root 
		while node:
			print (node.data)
			node = node.next
