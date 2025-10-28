class tryAdd:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return tryAdd(self.value+other.value)
    
    def __str__(self):
        return str(self.value)
a = tryAdd(10)
b = tryAdd(40)

print(a+b)