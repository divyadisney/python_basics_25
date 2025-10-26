# lambda -- used to excute single line instru
# map 
# filter

# def add(a,b):
#     c=a+b
#     return c
# print(add(10,5))

# lambda usage

# c=lambda a,b:a+b
# print(c(10,10))

# def multiply(num):
#     return num*2
# n=[10,20,30]
# for i in n:
#     print(multiply(i))

# map
# should be iteratable
# n=[10,20,30]
# print(list(map(lambda num:num*2,n)))

# n=[10,20,30,15]
# print(list(map(lambda num:True if num%2==0 else False,n))) 

#filter using map n lambda
n=[10,20,30,15]
print(list(filter(lambda num:True if num%2==0 else False,n))) 

lists=[10,20,30,15]
print(list(filter(lambda l:True if l*2==20 else False,lists)))

