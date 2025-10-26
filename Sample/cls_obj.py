# OOPs concepts

# __init__ calls automaticaly when object is created with class name
# self - reference of object

# class Student:
#     institute="One Team"             #class variale

#     def __init__(self):
#         print("Construts automatically when an object is called")
        
    
#     def getDetails(self,n,c):        
#         print(self)
#         self.name=n
#         self.course=c


# std1=Student()          #std1 - object creation 

# std1.getDetails("anna ","java")            #assinging values to object
# print(Student.institute)                     #assinging class variable
# print(std1.course)
# print(std1.name)




class Student:
    institute="One Team"             #class variale

    def __init__(self,n,c):
        print("Construts automatically when an object is called")
        print(self)
        self.name=n
        self.course=c
        
    
    def getDetails(self):        
        print("name:",self.name)
        print("course:",self.course)
        

std1=Student("Anna","Java")          #std1 - object creation 

# std1.getDetails("anna ","java")            #assinging values to object
print(Student.institute)                     #assinging class variable
# print(std1.course)
# print(std1.name)
std1.getDetails()


"""
class Student:
    institute="OneTeam" # class variable

    def __init__(self,n,c):
        print(self)
        self.name=n
        self.course=c

    def show_details(self):
        print("Name : ",self.name)
        print("Course : ",self.course)
        print("Age : ",self.age)

    def calculate_age(self):
        self.age=int(input("Enter your age : "))

std1=Student("Ebin","Java") # Object creation
std2=Student("Abhay","Python") # Object creation
print(Student.institute) # Accessing class variable
std1.calculate_age()
std2.calculate_age()
std1.show_details()
std2.show_details()
"""