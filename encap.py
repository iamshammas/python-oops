class Salary:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.__bonus = 2000

    def print_bonus(self):
        return f'Bonus: {self.__bonus}'
    
    def change_bonus(self,amount):
        self.__bonus=amount
        return self.__bonus
    
emp1 = Salary('Arun',4000)
print(emp1.print_bonus())
print(emp1.change_bonus(6999))
print(emp1.print_bonus())
