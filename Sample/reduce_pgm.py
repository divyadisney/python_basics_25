# reduce
from functools import reduce
num=int(input("Enter a number: "))
fact=reduce(lambda a,b:a*b,range(1,num+1))
print(fact)
