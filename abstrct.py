from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def cal_salary(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def get_basic_info(self):
        return f'Employee ID of {self.name} is {self.emp_id} '
    
class Fulltime_emp(Employee):
    def __init__(self, name, emp_id,salary):
        super().__init__(name,emp_id)
        self.salary = salary

    def cal_salary(self):
        return f'The salary of {self.name} with EMP ID {self.emp_id} is {self.salary}'
    
    def get_info(self):
        return f'FUll info: \nFull Name: {self.name} \nEMP ID: {self.emp_id} \nSalary: {self.salary}'
    

class Part_time_emp(Employee):
    def __init__(self, name, emp_id,hourly_wage,hours_worked):
        super().__init__(name, emp_id)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def cal_salary(self):
        salary = self.hourly_wage * self.hours_worked
        return f'Salary of Part time employee {self.name} is {salary}'
    
    def get_info(self):
        return f'PART TIME EMPLOYEE \nName: {self.name} \nEmp ID: {self.emp_id} \nSalary: {self.hourly_wage * self.hours_worked}'
    
full = Fulltime_emp('Adnan',123,12000)
part = Part_time_emp('Sinan',432,300,15)

print(full.get_info())
print(full.cal_salary())

print(part.get_info())
print(part.cal_salary())