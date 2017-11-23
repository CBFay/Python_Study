# properties.py
# Demonstration of Properties in Python
# From a stackabuse.com article on Python Properties
# Created on 11.23.2017 by CB Fay

# This is Python's way of creating getters, setters, and deleters.
class Person(object):
    def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
            
            @property
            def full_name(self):
                return self.first_name + ' ' + self.last_name
            
            @full_name.setter
            def full_name(self, value):
                first_name, last_name = value.split(' ')
                self.first_name = first_name
                self.last_name = last_name
                
            @full_name.deleter
n            def full_name(self):
                del self.first_name
                del self.last_name
                
x = Person('David', 'Cisneros')
print(x.first_name)
print(x.last_name)

x.full_name(self)
print(x.first_name)

# decorators are functions that take another function as an argument and add to its behaviour by wrapping it.

