# class is encapsuled with method and attributes
# Access specifies  -public private protected
# Unlike (Java or C++), Python doesn’t have strict enforcement of access specifiers. 
# Instead, it follows a naming convention to indicate the intended level of access.
# protected _,   private __

class A:
    def __init__(self):
        self._a=10

ob=A()
print(ob._a)  #can access but its not recommented since _ indicates protected

# class Student:
#     def __init__(self, name, age):
#         self.__age = age       # private variable
    
#     def show(self):
#         print("Age:", self.__age)  # Accessible inside class

# s = Student("Anna", 22)
# s.show()
# # print(s.__age)              # AttributeError: 'Student' object has no attribute '__age'

# #  But can be accessed indirectly using name mangling:
# print(s._Student__age)         # Not recommended, but possible
