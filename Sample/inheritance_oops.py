# Single inheritance

class Vehicle:
    count=0
    def rc_details(self,color,owner,brand,model):
        self.color=color
        self.owner=owner
        self.brand=brand
        self.model=model

class Cars(Vehicle):
    def __init__(self,gear,power,door):
        Vehicle.count+=1
        self.transmission=gear
        self.power=power
        self.door=door

    def display_details(self):
        print("Owner : ",self.owner)
        print("Model : ",self.brand+" "+self.model)
        print("Power : ",self.power)


car1=Cars("Manual","131 bph",5)
car1.rc_details("Black","Anna","Mahindra","Thar Roxs")
car1.display_details()

print(Vehicle.count)


"""
class Vehicle:
    count=0
    def __init__(self,color,owner,brand,model):
        self.color=color
        self.owner=owner
        self.brand=brand
        self.model=model

class Cars(Vehicle):
    def __init__(self,gear,power,door,color,owner,brand,model):
        super().__init__(color,owner,brand,model)
        Vehicle.count+=1
        self.transmission=gear
        self.power=power
        self.door=door

    def display_details(self):
        print("Owner : ",self.owner)
        print("Model : ",self.brand+" "+self.model)
        print("Power : ",self.power)

car1=Cars("Manual","131 bph",5,"Red","Raneesh","Mahindra","Thar Roxs")


car1.display_details()

print(Vehicle.count)
"""

# Multiple Inheritance  - one child class can inherit 2 or more parent class

"""class Animal():
    def animalSound(self):
        print("Some animal makes sound")

class AquaAnimal():
    def aquaAnimal(self):
        print("Some aqua animal makes sound")
class Mammal(Animal, AquaAnimal):
    def mammal(self):
        print("Blue whale lives in water and makes sound")

obj=Mammal()
obj.animalSound()
obj.aquaAnimal()
"""
# Multilevel inheritance - class derived from other class

"""class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C(B):
    def c(self):
        print("C")

obj=C()
obj.a()
obj.b()
obj.c()"""

# Hierarchical Inheritance

"""class Name:
    def __init__(self,name):
        self.n=name

class Emp(Name):
    def role(self):
        print(f"{self.n} works as employee")

class dept(Name):
    def admin(self):
        print(f"{self.n} works in admin dept")

obj=Emp("Anna")
obj.role()
o1=dept("Anna")
o1.admin()"""

