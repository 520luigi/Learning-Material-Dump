
# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay): #constructor, initialize all the class variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

emp_1 = Employee("Lindsay", "Damiano", 88888)
emp_2 = Employee("Luigi", "Zheng", 88888)

print(emp_1)
print(emp_2)

print(Employee.fullname(emp_1)) #same as the one bellow of fullname function...
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
