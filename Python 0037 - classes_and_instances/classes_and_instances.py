# From https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=255s
# Corey Shafer's tutorial on Classes and Instances
# Created on 11.23.2017 by CB Fay

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last
        

emp_1 = Employee('Adam', 'Grange', 50000)

print emp_1.fullname()
print emp_1.email

print(Employee.fullname(emp_1))
