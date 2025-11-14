import pickle
from tabulate import tabulate
student_details=[["Name","Id","Email","English","Hindi","Maths","Science"]]
student_header=["Name","Id","Email","English","Hindi","Maths","Science"]

def AddStudent():
    ["Name","Email","English","Hindi","Maths","Science"]
    studentCount=int(input("\nEnter the number of students to be entered: "))
    stud_id=len(student_details)
    for i in range(studentCount):
        student_name=input("\nEnter the name of the student: ")
        student_email=input("Enter the email of the student: ")
        stud_mark_eng=int(input("Enter the mark(English) :"))
        stud_mark_hin=int(input("Enter the mark(Hindi) :"))
        stud_mark_math=int(input("Enter the mark(Maths) :"))
        stud_mark_sci=int(input("Enter the mark(Science) :"))
        student_details.append([student_name,stud_id+i,student_email,stud_mark_eng,stud_mark_hin,stud_mark_math,stud_mark_sci])
    with open("Student_detalails_file","wb") as student_file:
        pickle.dump(student_details,student_file)


def SearchStudent():
    with open("Student_detalails_file","rb") as search_student:
        search_file=pickle.load(search_student)
        print("\nSerach by:\n1.Id\n2.Name\n3.Email")
        choice=int(input("Enter your choice:"))
        match choice:
            case 1:
                stud_id=int(input("Enter the id :"))
                for sid in search_file[1:]:
                    if sid[1] == stud_id:               
                        studentId=[]
                        studentId.append(sid)
                        table_id_output=tabulate(studentId,headers=student_header,tablefmt="grid")
                        print(table_id_output)
                        break
            
            case 2:
                stud_name=input("Enter the name of the student :")
                for name in search_file[1:]:
                    if str(name[0]) == stud_name:
                        studentName=[]
                        studentName.append(name)
                        table_name_output=tabulate(studentName,headers=student_header,tablefmt="grid")
                        print(table_name_output)
                        break

            case 3:
                stud_email=input("Enter the email of the student :")
                for studemail in search_file[1:]:
                    if(str(studemail[2])) == stud_email:
                        studentEmail=[]
                        studentEmail.append(studemail)
                        table_email_output=tabulate(studentEmail,headers=student_header,tablefmt="grid")
                        print(table_email_output)
                        break

            case __:
                print("*****Invalid Choice*****")

      

                        
                    
