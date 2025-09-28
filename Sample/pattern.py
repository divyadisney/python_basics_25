"""
*
* *
* * *
* * * *
* * * * *

"""

"""
1
2 3
4 5 6 
7 8 9 10
11 12 13 14 15
"""

# n=1
# for i in range(1,6):
#     for j in range(1,i+1):
#       print(n,end=" ")
#       n=n+1
#     print(" ")   


"""
1
7 6
14 13 12
21 20 19 18
28 27 26 25 24
"""

"""
7
14 13
21 20 19
28 27 26 25
"""

# r=5
# n=7
# for i in range(1, r+1):
#    for j in range(1,i):
#          print(n,end=" ")
#          n=n-1
#    n=i*7
#    print(" ")


# print("\n")
# r=5
# n=1
# for i in range(1, r+1):
#    n=i*7
#    for j in range(1,i+1):
#          print(n,end=" ")
#          n=n-1
#    print(" ")

print("\n")
r=5
n=1
for i in range(1, r+1):
   for j in range(1,i+1):
         print(n,end=" ")
         n=n-1
   n=i*7       
   print(" ")


   """
   1
   2 6
   3 7 10
   4 8 11 13
   5 9 12 14 15

   """
# print("\n")
# r=5
# n=1
# for i in range(1,r+1):
#      for j in range(1,i+1):
#           print(n,end=" ")   
#           n=(n+r)-j
#      n=i+1
#      print()       


"""
 A
 B C
 D E F
 G H I J
"""    

# print(chr(65))
# r=5
# n=65
# for i in range(1,r+1):
#      for j in range(1,i+1):
#           print(chr(n),end=" ")
#           n=n+1
#      print("")

"""
A
A B
A B C
A B C D 
"""

# print()
# r=5
# for i in range(1,r+1):
#      n=65
#      for j in range(1,i+1):
#           print(chr(n),end=" ")
#           n=n+1
#      print()  

"""
        A
      A B
    A B C 
  A B C D
A B C D E 

"""

for i in range(5,3,-1):
     print()


# r=5
# for i in range(1,r+1):
#      for j in range(1,r-i+1):
#           print(" ",end=" ")
#      for k in range(1,i+1):
#           print(k,end=" ")
#           k=k+1
#      print()  

# print()
# r=6
# for i in range(1,r+1):
#      n=65
#      for j in range(1,r-i+1):
#           print(" ",end=" ")
#      for k in range(1,i+1):
#           print(chr(n),end=" ")
#           n=n+1
#      print()  

"""
      1
     123
    12345
    
"""
n=1
r=5
for i in range(1,r+1):
     for j in range(1,(r-i)//2+1):
          print(" ",end=" ")
     for k in range(1,i+1):
          print(k,end=" ")
          k=k+1
     print()

# reverse of a string

# str="String"
# s=""
# for i in str:
#      s=i+s
#      print(s)
# print(s)     