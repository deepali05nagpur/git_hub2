# modified
class A():
    no_of_leaves=8
    _pro=9
    __pri=10
    def __init__(self,ename,esal,erole):
        self.name=ename
        self.salary=esal
        self.role=erole
        
    def info(self):
        print(f"name of employe is {self.name}")
        print(f"Salary of employe is {self.salary}")
        print(f"role of employ {self.role}")

a=A("raj",1000,"AQ12")
a.info()

    
        
        
