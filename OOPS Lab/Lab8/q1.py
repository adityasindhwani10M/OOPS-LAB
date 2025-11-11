'''
class Company:
    def __init__(self):
        self.name="PYnative"
        self.address="ABC Street"
    def show(self):
        print('Name :',self.name,'Address :',self.address)

cmp=Company()
cmp.show()
'''
'''
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def show(self):
        print(f"Name : {self.name}.. Age : {self.age}.. Salary : {self.salary}")
    
emma=Employee('Emma',23,75000)
emma.show()
kelly=Employee('Kelly',25,7100)
kelly.show()
'''
'''
class Student:
    def __init__(self,name):
        self.name=name
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age,sep='\n')
# emma=Student('Emma')
kelly=Student('Kelly',25)
kelly.show()
'''