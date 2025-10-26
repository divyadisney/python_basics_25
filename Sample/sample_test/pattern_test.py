"""
      1
    2 3
  3 4 5
4 5 6 7
"""
# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#        print(" ",end=" ")
#     for k in range(i,i+i):
#        print(k,end=" ")
#        k=k+1
#     print()

"""
    1
  2 3 4
3 4 5 6 7
"""
# num=1
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    for k in range(1,2*i):
#       print(num,end=" ")
#       k=k+1
#       num=num+1
#    print()

"""
    1
  2 3 4
3 4 5 6 7
  8 9 10
    11
"""
# num=1
# for i in range(1,5+1):
#    for j in range(1,5-i+1):
#       print(" ",end=" ")
#    for k in range(1,2*i):
#       print(num,end=" ")
#       k=k+1
#       num=num+1
#    print()
# for i in range(1,5+1):
#    for j in range(1,5-i+1):
#       print(num,end=" ")
#       k=k+1
#       num=num+1
#    for k in range(1,2*i):
#       print(" ",end=" ")
      
#    print()

num=1
n=int(input("Enter a number :"))
for i in range(1,n+1):
   for j in range(1,n-i+1):
      print(" ",end=" ")
   for k in range(1,2*i):
      print(num,end=" ")
      k=k+1
      num=num+1
   print()