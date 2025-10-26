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