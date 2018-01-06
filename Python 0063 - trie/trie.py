# Personal implementation of a Trie
# Created 01.06.2018 by CB Fay

class Node:
    def __init__(self, data=''):
        self.data = data
        self.branches = []
    
    def __repr__(self):
        return self.data
        
    def add(self, data, prefix=''):
        """Insert a String"""
        if len(data) == 0:
            return True
        else:
            for branch in self.branches:
                if prefix+data[0] == branch.data:
                    branch.add(data[1:], branch.data)
                    return
            self.branches.append(Node(prefix+data[0]))
            self.branches[-1].add(data[1:], prefix=prefix+data[0])
            return
    
    def inorder(self):
        """Print the value of each leaf"""
        if self.branches == []:
            print(self.data)
            return
        else:
            for branch in self.branches:
                branch.inorder()
    
    def ataddress(self, addr):
        """Navigate to a specific node with a list of indices"""
        try:
            if len(addr) == 1:
                return self.branches[addr[0]].data
            return(self.branches[addr[0]].ataddress(addr[1:]))
        except IndexError:
            print('Error: Invalid Address')
            return False
        
class Trie:
    def __init__(self, data=None):
        self.root = Node()
        if data:
            self.root.add(data)
    
    def add(self, data):
        self.root.add(data)
        
    def inorder(self):
        self.root.inorder()
        
    def ataddress(self, addr):
        return(self.root.ataddress(addr))
