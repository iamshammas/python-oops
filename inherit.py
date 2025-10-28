

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def show_details(self):
        print(f'The salary of {self.name} is {self.salary} ')

class Manager(Employee):
    def __init__(self, name, salary,department):
        Employee.__init__(self,name,salary)
        self.department=department
        self.team_size = 0


e1 = Employee('Arun',70000)

e1.show_details()