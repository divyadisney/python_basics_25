# Polymorphism - Compile time(Method overloading) and run time(method over riding)
# runtime polymorphism

class Animal:
    def sound(self):
        print("Generic sounds")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Dog(Animal):
    pass

c=Cat()
c.sound()

d=Dog()
d.sound()

