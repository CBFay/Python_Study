# linked_list.py
# Ongoing implementation of a Singly Linked List
# Created on 11.27.2017 by CB Fay
# Updated on 12.02.2017

class node:
	"""Node object used to implement Linked Lists"""
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
	def __str__(self):
		return str(self.data)

	def remove(self):
		if self.next:
			self.data = self.next.data
			self.next = self.next.next
			return True
		return False
		
class linked_list:
	"""Singly Linked List object"""
	
	def __init__(self):
		"""Create a linked_list object given no parameters."""
		self.root = None # this will change every time we add a new node.
		self.size = 0
	
	def __init__(self, sequence): # O(k)
		"""Create a linked_list object given a iterable object."""
		self.root = None
		self.size = 0
		for i in range(1, len(sequence)+1, 1):
			self.add(sequence[-i])
			
		
	def __len__(self):
		"""Implement the built-in function len().
		Return the number of list elements
		"""
		return self.size
		
	def __str__(self):
		"""Implement the built-in function str().
		Return the informal string representation of self.
		"""
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
		"""Implement evaluation of self[key]"""
		if index < 0:
			distance = self.size + index
		else:
			distance = index
		node = self.root
		for i in range(distance):
			node = node.next
		return node
		
	def add(self, value):
		"""Insert a node with a given value at the head of the list"""
		new_node = node(value, self.root) # create a new node
		self.root = new_node # set the root node to the one we just added
		self.size += 1
		
	def extend(self, elements):
		for x in elements:
			self.add(x)
	
	# is buggy
	def remove(self, deleteme):
		"""Remove all instances of a given value from the list"""
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
		"""Use a hashset to remove duplicate elements"""
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
				
	def kth_from_last(self, k):
		"""Return the node k elements from the tail of the list.
		This is useful if self.size doesn't exist.
		"""
		a = self.root
		b = self.root
		for i in range(k):
			b = b.next
		while b:
			a = a.next
			b = b.next
		return a
