class Node:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None
		
	def insert(self, data):
		if self.value == data:
			return False
		elif self.value > data: # LEFT
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
				return True
		elif self.value < data: # RIGHT
			if self.right: 
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True
				
	def find(self, data):
		if self.value == data:
			return True
		elif self.value < data: # LEFT
			if self.left:
				return self.left.find(data)
			else:
				return False
		elif self.value > data: # RIGHT
			if self.right:
				return self.left.find(data)
			else:
				return False
	
	def preorder(self):
		if self:
			print(str(self.value), end = ' ') # print top down
			if self.left:
				self.left.preorder()
			if self.right:
				self.right.preorder()

	def postorder(self):
		if self:
			if self.left:
				self.left.postorder()
			if self.right:
				self.right.postorder() # print bottom up
			print(str(self.value), end=' ') 
			
	def inorder(self):
		if self:
			if self.left:
				self.left.inorder()
			print(str(self.value), end = ' ') 
			if self.right:
				self.right.inorder() 


		
class Tree:
	def __init__(self):
		self.root = None
		
	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True
   
	def find(self, data):
		if self.root:  
			return self.root.find(data)
		return False # else
	
	def preorder(self):
		print("Preorder")
		self.root.preorder()

	def postorder(self):
		print("PostOrder")
		self.root.postorder()
		
	def inorder(self):
		print("InOrder")
		self.root.inorder()
