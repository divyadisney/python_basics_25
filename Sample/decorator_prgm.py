# def dec(fun):    # fun -->  greet  function
#     def wrapper():
#         print("Nested function called")
#         fun() # This part calls the greet function which passed while calling
#     return wrapper

# # @dec
# def greet():
#     print("Hello")

# f=dec(greet)   # f  -->  wrapper function
# f()
# greet()


#    Program 2

# def loginRequired(fun):
#     def wrapper(n,status):
#          if status:
#              fun(n,status)
#          else:
#             print("Invalid user")
#     return wrapper

# def Dashboard(name,is_authenticated):
#     print("Welcome ",name)

# k=loginRequired(Dashboard)
# print(k)
# k('Roshin',True)

# def loginRequired(fun):
#     def wrapper(name,is_authenticated):
#          if is_authenticated:
#              fun(name,is_authenticated)
#          else:
#             print("Invalid user")
#     return wrapper

# @loginRequired
# def Dashboard(name,is_authenticated):
#     print("Welcome ",name)
# Dashboard("Anna",True)



# def loginRequired(fun):
#     def wrapper(name,is_authenticated):
#          if is_authenticated:
#              fun(name,is_authenticated)
#          else:
#             print("Invalid user")
#     return wrapper


# def Dashboard(name,is_authenticated):
#     print("Welcome ",name)


# w=loginRequired(Dashboard)
# w(name="Anna",is_authenticated=True)



# def checker(fun):
#     def wrapper(a,b):
#         if a>b:
#             return fun(a,b)
#         else:
#             return "a is smaller"
#     return wrapper

# @checker
# def substract(a,b):
#     return a-b

# print(substract(6,7))



def returneven(fun):
    def wrapper(n):
        if n%2==0:
            return f"{n} is even"
        else:
            return f"{n} is odd"
    return wrapper

def evenodd(n):
    return n

w=returneven(evenodd)
print(w(4))

