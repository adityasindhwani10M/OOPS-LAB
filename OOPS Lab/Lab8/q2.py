class Parent:
    def __init__(self,name):
        self.name=name
        print("Parent constructor called. Name :",self.name)

class Child(Parent):
    def __init__(self,name,age):
        # call parent constr.
        super().__init__(name)
        self.age=age
        print("Child constructor called. Age :",self.age)

child=Child("Alice",10)
