#object oriented programming is just like the name. It is a modeling type programming
#where your codes are interconnected. For example, you have an object or class of employee,
#now you want variables like first name, last name, pay, email, etc. So you make these
#classes or objects as a blueprint, for simplying codes.

#encapsulate data and behavior into one unit:
#--easier to maintain, faster development, modular structure
#4 pillars: encapsulation, abstraction, inheritance, polymorphism

#"best functions are those with no parameters!"

# encapsulation: act of combining properties and methods, related to the same object

# abstraction: more generic than ecapsulation

# inheritance: eliminate redundant code, codes inherit properties

# polymorphism: many forms or usage of methods. The method usage changed depending on
#               what objects are called...not sure what this really means need to check this out

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    #method are just functions inside a class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Hello', 'World', 42)

# print(emp_1)
# print(emp_2)

print(emp_1.fullname())
