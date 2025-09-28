# while loop

# Multiplication table
# a=int(input("Eneter a number:"))
# i=1
# while(i<11):
#     print(i," * ",a,"=",a*i)
#     i=i+1


# print("\n***Calculator***")
# while True:
    
#     a=int(input("\nEnter the first number :"))
#     b=int(input("Enter your second number :")) 
#     print("\n1.Add\n2.Sub\n3.Multiply\n4.Divide\n")
#     c=int(input("Enter your choice:\n"))
#     match c:
#         case 1:
#             print(a+b)
#         case 2:
#             print(a-b)
#         case 3:
#             print(a*b)
#         case 4:
#             print(a/b)
#         case __:
#             print("Invalid input")
#     d=input("Do you need to continue (y/n) :")
#     if d!="y":
#             break
    

# First 3 multiples divisible by both 6 and 7


i=1
count=0
while(i < 500):
    if(i%7==0 and i%6==0):
         print(i)
         count=count+1
         if count==3:
          break   
    i=i+1




