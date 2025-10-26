# resursion
def fun(num):
    if num==1:
      return 1
    else:
       print(num)
       num=num-1
       return fun(num)
print(fun(5))   

def fun(fact):
   if fact==0:
      return 1
   else:
      print(fact)
      return fact * fun(fact-1) 
print(fun(5))


