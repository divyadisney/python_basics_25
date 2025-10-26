# Functions -------- keyword def

# def greeting():
#     print("Hello world")
# greeting()

# def nameFunction(name, age):
#     print("Hello",name,"you are",age,"years old")
# nameFunction("Anna",15)

# def nameFunction(name, age, course="java"):
#     print("Hello",name,"you are",age,"years old","\nCourse choosen is",course)
# nameFunction("Anna",15)
# nameFunction("Biya",25,course="python")

# def nameFunction(name, age, course="java"):
#     print("Hello",name,"you are",age,"years old","\nCourse choosen is",course)
# nameFunction("Anna",15)

# Non-keyword args and keyword args
#      **kargs and *args

# def nameAge(**kargs):
#     print("Hello",kargs.get('name'),"you are",kargs.get("age"))
# nameAge(name="Anna",age=15)

# def add(*args):
#     s=0
#     for k in args:
#         s=s+k
#     print(s)

# add(10,20,30)
# def evenodd(n):
#     if n%2==0:
#         return True
    
# print(evenodd(10))

def newFunction(*args):
    n=0
    if n%2==0:
        return "yep"
    # else:
    #     return "nope"
    
print(newFunction(2))


# for k in range(1,4):
#     print(newFunction(input("Enter a number:")))

def f1():
    s = 'Function'
    def f2():
        print(s)
        
    f2()
f1()

