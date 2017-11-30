# linked_list.py
# Growing implementation of a Linked List
# Created on 11.27.2017 by CB Fay
# Updated on 11.29.2017 by CB Fay

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
		
	def add(self, data):
		new_node = node(data, self.root) # create a new node
		self.root = new_node # set the root node to the one we just added
		self.size += 1
	
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
			prev = self.root
			node = node.next
			inlist.add(prev.data)
			while node.next:
				if node.data in inlist:
					prev.next = node.next
					node = node.next
				else:
					inlist.add(node.data)
					node = node.next
					prev = prev.next
			if node.data in inlist: # if the tail is a duplicate, delete it
				prev.next = None
		
	def list_print(self):
		node = self.root 
		while node:
			print (node.data)
			node = node.next
