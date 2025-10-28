class Car():
    def __init__(self,name,year,price,color):
        self.name = name
        self.year = year
        self.price = price
        self.color = color
    
    def __str__(self):
        res = f'{self.name} {self.year} {self.color} - {self.price}'
        return res

car1 = Car("Toyota Corolla", 2020, 20000, "Red")

print(car1)

class Dog():
    def __init__(self,name):
        self.name = name
    def barks(self):
        return f'{self.name} is barking!!'
    
print(Dog('Hippy').barks())