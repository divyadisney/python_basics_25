# condition if
# age=int(input("Enter your age: "))
# if age>=18:
#      print("Eligible to vote")
# else:
#      print("Not eligible")

# odd even  if statement
# a=int(input("Enter a number:"))
# if a%2==0 :
#     print(a," is even")
# else:
#     print(a," is odd")

# elif

# a= int(input("Enter 1st no. :"))
# b= int(input("Enter 2nd no. :"))
# print("1.Add\n 2.Sub\n 3.Multiply\n 4.Divide")
# choice = int(input("Enter the choice: "))
# if choice==1:
#     print(a+b)
# elif choice==2:
#     print(a-b)
# elif choice==3:
#     print(a*b)
# elif choice==4:
#     print(a/b)
# else:
#     print("Not between 1-4")


# match
# a= int(input("Enter 1st no. :"))
# b= int(input("Enter 2nd no. :"))
# print("1.Add\n 2.Sub\n 3.Multiply\n 4.Divide")
# choice = int(input("Enter the choice: "))
# match choice:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a*b)
#     case 4:
#         print(a/b)
#     case __:
#         print("Invalid")

# Nested if
a=int(input("Enter a number: "))
if a%2==0:
    print(a," divisible by 2")
    if a%2==0 and a%3==0:
        print(a, " is divisible by 2 and 3")
else:
    print("Not divisible by both")
