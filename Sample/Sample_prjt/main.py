from tabulate import tabulate
from student import AddStudent,SearchStudent
import pickle


while True:
    print("\n1.Add Student\n2.View All Student\n3.Search Student\n4.Update Student\n5.Delete Student\n6.Generate Student Report\n7.Exit ")
    a=int(input("Enter your choice:"))
    match a:
        case 1: 
            AddStudent()
        case 2:
            print("\n\t****Alert Only Authenticated Users Can Open*****")
            auth_username=input("Enter username:")
            auth_psd=input("Enter password:")
            try:
                with open("auth_file","rb") as auth_files:
                    auth_loaded=pickle.load(auth_files)
                auth=False
                for user_data in auth_loaded:
                    if user_data.get("username")==auth_username and user_data.get("password")==auth_psd:
                            auth=True
                            break
                if auth==True:
                            print("\n\t**Authentication Success**\n")    
                            with open("Student_detalails_file","rb") as student_file:
                                studentFile=pickle.load(student_file)
                                table_output=tabulate(studentFile,headers="firstrow",tablefmt="grid")
                                print(table_output)
                else:
                        print("\n\t**Authentication Failure**\n")
            except Exception as e:
                print("\n\tAn error found",e)
        case 3:
            SearchStudent()
        # case 4:
        #     UpdateStudent()
        # case 5:
        #     DeleteStudent()
        # case 6:
        #     GenrateStudentReport()
        case 7:
            print("-------Exiting--------")
            break
        case _:
            break

        
