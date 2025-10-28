# Create a class called Animal with the following properties:
# name: A string that stores the animal's name.
# age: An integer that stores the animal's age.
# The class should also have the following methods:
# speak(): This method prints a message to the console that says the animal's name and age.
# Create two subclasses of Animal: Dog and Cat.
# The Dog class should have an additional property called breed.
# The Cat class should have an additional method called meow() that prints a message to the console that says "Meow!".
# Create an object of each type and call the speak() method on each object.


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        return f'Age is {self.age} and name is {self.name}'
    

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self):
        return "Meow!"
    
dogg = Dog('Sunny',4,'American')
catt = Cat('Mussi',2)

print(dogg.speak())
print(catt.speak())
print(catt.meow())
