# Implementation of a Hashmap
# Created 1.12.2018 by CB Fay

class Hashmap:
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size
        
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
        
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                if len(self.map[key_hash]) == 0:
                    self.map[key_hash] = None
                return True
        return False
    
    def print(self):
        for item in self.map:
            if item is not None:
                print(item)
                
h = Hashmap()
h.add('Tom', '374-854-9981')
h.add('Banks', '275-684-9445')
h.add('Lisa', '155-664-3485')
h.add('John', '465-738-1847')
h.add('Susan', '222-847-5879')

h.delete('Tom')

h.print()
