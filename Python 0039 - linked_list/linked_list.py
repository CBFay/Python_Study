# linked_list.py
# Implementation of a Linked List
# Created on 11.27.2017 by CB Fay

class node:
	def __init__(self):
		self.data = None
		self.next = None
	def __str__(self):
		return str(self.data)
		
class linked_list:
	def __init__(self):
		self.root = None # this will change every time we add a new node.
		
	
	def add(self, data):
		new_node = node() # create a new node
		new_node.data = data
		
		new_node.next = self.root # link the new node to the 'previous' node.
		self.root = new_node # set the current node to the new one.
		
	def list_print(self):
		node = self.root 
		while node:
			print (node.data)
			node = node.next
			
