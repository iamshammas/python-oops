# --- Vehicle Info ---
# Brand: Generic Vehicle
# Speed: 60 km/h
# Engine started (generic vehicle)

# --- Car Info ---
# Brand: Tesla
# Speed: 120 km/h
# Fuel Type: Electric
# Car engine started with Electric


class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        return f'Brand: {self.brand} \nSpeed: {self.speed} km/h'

    def start_engine(self):
        return f"Engine started (generic vehicle)"

class Car(Vehicle):
    def __init__(self, brand, speed,fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show_info(self):
        br = super().show_info()
        return f'{br} \nFuel Type: {self.fuel_type}'
        # return f'Brand: {self.brand} \nSpeed: {self.speed} km/h \nFuel Type: {self.fuel_type}'
    
    def start_engine(self):
        return f'Car Engine Started with {self.fuel_type}'
    

v1 = Vehicle("Generic Vehicle", 60)
c1 = Car("Tesla", 120, "Electric")


print(v1.show_info())
print(v1.start_engine())
print('=====================')
print(c1.show_info())
print(c1.start_engine())
