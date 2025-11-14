
# We can only access abstract(parent) via child class and not directly
# from abc import ABC,abstractmethod

# class A(ABC):
#     @abstractmethod
#     def display(self):
#         print("Hello")   # method declared but not defined

# class B(A):
#     def display(self):
#         print("Hi")     # defined in subclass

# ob=B()
# ob.display()


"""
from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def display(self):
        print("Hello")

class B(A):
    def display(self):
        super().display()   #access parent class
        print("Hi")

ob=B()
ob.display()"""


"""from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Car engine started")

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        pass

    def stop(self):
        print("Car engine stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike engine stopped")

car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()
"""

from abc import ABC#, abstractmethod
class Bank(ABC):
    # @abstractmethod
    def personalDetails(self):
        print("These are personal")

    def bnakhold(self):
          print("I am bank holder")

class AccountName(Bank):
    def personalDetails(self):
        n="Anna"
        print(f"{n} holds the account")

print()
obj=AccountName()
obj.personalDetails()
obj.bnakhold()