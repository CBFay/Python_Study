https://www.youtube.com/watch?v=YlgPi75hIBc

class Node:
    def__init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
        elif self.value < data:
            if right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
    def find(self, data):
        if self.value == data:
            return False
        elif self.value < data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        elif self.value > data:
            if self.right:
                return self.left.find(data)
            else:
                return False
    
        

        
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root.insert(data)
    def find(self, data):
        if self.root:  
            return self.root.find(data)
        return False
