
# file handling it uses w - write, r - read, a - append
file=open("std_detalis.txt","w")          # opens a new file ore rewrites the new file
file.write("\nPython")
file.close()


"""
file=open("std_detail.txt","w")
file.close()

def addStudent():
    name = input("Enter your name : ")
    course = input("Enter your course : ")
    age = int(input("Enter your age : "))
    file=open("std_detail.txt","a")
    file.write(f"{name}--{course}--{age}\n")
    file.close()
def readData():
    file = open("std_detail.txt", "r")
    data = file.readlines()
    for k in data:
        print(k.split("--"))
    file.close()
while True:
    print("1.Add Student\n2.Display students\n3.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        addStudent()
    elif choice==2:
        readData()
    elif choice==3:
        break
    else:
        print("Invalid input")
"""