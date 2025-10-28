class Employee():
    def __init__(self,name,designation,salary,address):
        self.name = name
        self.designation = designation
        self.salary = salary
        self.address = address
    
    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}'

    def came(self):
        print(f'{self.name} entered to office')

    def went(self):
        print(f'{self.name} went out from office')

    def change_address(self,new_address):
        self.address=new_address


emp1 = Employee('Arun','Engineer',10000,'Palakkad')

# print(emp1.came())

print(emp1)
print('-------------------------')
emp1.came()
print('-------------------')
emp1.change_address('Calicut')
print(emp1)