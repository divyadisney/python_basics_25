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


# """
# 1
# 2 1
# 3 2 1
# 4 3 2 1

# """
# n=int(input("Enter a num: "))
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#         i=i-1
#     print()


# """
# 2
# 3 5
# 7 11 13
# 17 19 23 29


# """

# n=50
# count=0
# l=[]
# for j in range(2,n):
#     for i in range(2,j):
#         if(j%i == 0):
#             break
#     else:
#         p=j
#         l=l+[p]
# c=0
# for i in range(1,5+1):
#     for k in range(i):
#        print(l[c],end=" ")
#        c=c+1
#     print()

# palindrome
# s=input("enter a string: ")
# if s==s[::-1]:
#     print(f"{s} is panlindrome")
# else:
#     print("Not palinddrome")

# s=int(input("Enter a nmber: "))
# num=str(s)
# if num==num[::-1]:
#     print("palindrome")
# else:
#     print("not")
