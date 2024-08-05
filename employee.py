class Employee:
    def __init__(self,role,dept,salary):
        self.role =role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(f"{self.role}\n{self.dept}\n{self.salary}")

class Engineer(Employee):
    def __init__(self, name,age):

        self.name =name
        self.age =age
        super().__init__("developer","IT","70000")


E1 = Engineer("Me",22)
E1.showDetails()
print(E1.age)