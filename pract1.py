class Employee:
    def __init__(self,nme,sal,ag) :
        self.name=nme
        self.salary=sal
        self.age=ag

    def get_info(self):
        print("Employee name is ",self.name)
        print(f"Employee salary is {self.salary}")
        print(f"Employee age is {self.age}")
        
e1=Employee("nitin",23000,45)
e1.get_info()
print(getattr(e1,"age"))
print(setattr(e1,"name","ewa"))
print(e1.__dict__)

# done changes for git weite only commemt
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"my name is {self.name} and age is {self.age}")
p=person("Deepali",34)
p.info()



