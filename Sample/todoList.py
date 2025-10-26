taskList=[]    

def addtask():
    taskCount=int(input("\nHow many task you wish to enter:"))
    startId=len(taskList)+1
    for i in range(taskCount):
        myTask=input("Enter the task:")
        # taskList.append(myTask)
        taskList.append([myTask, False,startId+i])
    # print(taskList)
    return taskList
    
# def showTask():
#     print("\nTasks")
#     for i,n in enumerate(taskList,1):
#         print(f"{i} {n} ")
#     print()
# def showTask():
#     print("\nTasks")
#     for i, n in enumerate(taskList, 1):
#         status = "Done" if n[1] else "Incomplete"
#         print(f"{i} {n[0]} - {status}")     #1 python - incomplete
#     print()
def showTask():             #new code
    print("\nTask")
    for i in taskList:
        status="Done" if i[1] else "Incomplete"
        print(f" {i[2]} {i[0]} - {status}")
    print()


# def removeTask():  #old code
    # taskId=int(input("Enter the task Id: "))   
    # if 0 < taskId <= len(taskList):
    #     taskList.pop(taskId-1)
    # showTask() 
def removeTask():
    taskId=int(input("Enter the task Id that should be removed:"))
    for i in taskList:
        if i[2] == taskId:
            taskList.pop(taskId-1)
    showTask()        


# def updateTask():
#     taskId=int(input("Enter the task id: "))
#     if 0 < taskId <= len(taskList):
#         taskList[taskId - 1][1] = not taskList[taskId - 1][1]  
#         print("Task Updated \n")
#     else:
#         print("Invalid Task ID!\n")   
#     showTask()
def updateTask():               #new code
    taskid=int(input("Enter the task id that should be updated: "))
    for i in taskList:
        if i[2] == taskid:
            i[1] = not i[1] 
    else:
        print("Invalid Input!")    
    showTask()


while True:
    print("ToDo Tasks")
    print("1. Add task \n2. Update Task \n3. Remove Task \n4. Show Task \n5. Exit")
    c=int(input("Enter your choice: "))
    match c:
        case 1:
            addtask()
        case 2:
            updateTask()
        case 3:
            removeTask()
        case 4:
            showTask()
        case 5:
            print("*********Exiting*********")  
            break
        case __:
            print("Invalid Input")  
        

# edit code with id specifed in list itself , unique id for every element

"""

def addTask(tasks):
    task_count=int(input("Enter how many task do you wish to enter : "))
    if tasks:
        new_id=max(tasks.keys())+1
    else:
        new_id=1
    for k in range(1,task_count+1):
        task=input(f"Enter the task {k} : ")
        tasks[new_id]={"task":task,"status":False}
        new_id+=1
    return tasks

def showTask(todos):
    for id,task in todos.items():
        status='Complete' if task['status'] else 'Incomplete'
        print(f"{id} --  {task["task"]} --  {status}")

def updateTask(todos):
    edit_task_id=int(input("Enter the task id to be updated : "))
    if edit_task_id in todos:
        edit_task=todos.get(edit_task_id)
        edit_task["status"]=not edit_task["status"]
        print("Task updated successfully")
        showTask(todos)
        return todos
    else:
        print("Id not found")
        return todos

todos={}
while True:
    print("1.Add task\n2.Update Task\n3.Delete task\n4.Display task\n5.Exit")
    try:
        choice=int(input("Enter your choice : "))
    except ValueError:
        print("Please enter valid choice number : ")
    except Exception as e:
        print(e)
        
    if choice==1:
        todos=addTask(todos)
    elif choice==2:
        todos=updateTask(todos)
    elif choice==4:
        showTask(todos)
    elif choice==5:
        break
"""