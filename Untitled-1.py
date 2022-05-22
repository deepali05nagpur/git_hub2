class Employee:
    def __init__(self,e_name,e_sal,e_age) :
        self.name=e_name
        self.salary=e_sal
        self.age=e_age

    def get_info(self):
        print(f"Employee name is {self.e_name}")
        # print(f"Employee salary is {self.e_sal}")
        # print(f"Employee age is {self.e_age}")
        
e1=Employee("nitin",23000,45)
e1.get_info()
print(e1.__dict__)