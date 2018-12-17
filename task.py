import os.path
if not os.path.exists("task.txt"):
    file=open("task.txt","w")
    file.close()
def findtask(choice3,x,y):
    for i in range(len(choice3)):
        if i!=y and choice3[i][0]==x:
            return True
    return False
file=open("task.txt","r")
data=file.read()
file.close()
ListOfTasks=data.split("--task--")
ListOfTasks.pop(0)
for cnt in range(len(ListOfTasks)):
    ListOfTasks[cnt]=list(ListOfTasks[cnt].split("--subtask--"))
choice="A"
choice2=""
choice3=0
choice4=0
Task=""
Subtask=""
DOC=""
while True:
    choice=input("Enter your choice to Add/Remove/View/Replace/Edit/Save/SaveAndExit/Exit/Delete (A/R/V/RE/ED/S/SE/E/D):")
    choice=choice.upper()
    if choice=="E":
        print("Exited Successfully")
        break
    elif choice=="A":
        print("You can add multiple tasks or subtasks here.")
        choice2=input("Enter your choice to add a task or subtask on existing task (T/S):")
        choice2=choice2.upper()
        if choice2=="S":
            choice3=input("Enter the number of task(number of tasks present in current list:"+str(len(ListOfTasks))+"):")
            if choice3.isnumeric():
                choice3=int(choice3)
                if choice3==0 or choice3>len(ListOfTasks):
                    print("Sorry we couln't find any such task in list or number is wrong.")
                    continue
                else:
                    while True:
                        choice4=input("Enter the position(number) of your subtask(Enter only to stop adding)(number of subtasks in task("+str(choice3)+"):"+str(len(ListOfTasks[choice3-1])-2)+"):")
                        if choice4.isnumeric():
                            choice4=int(choice4)
                            if choice4==0 or choice4>len(ListOfTasks[choice3-1])-1:
                                print("Sorry we couln't find any such position(subtask) in list or number is wrong.")
                                continue
                            else:
                                Subtask=input("Enter your subtask:")
                                ListOfTasks[choice3-1].insert(choice4+1,Subtask)
                                print("Subtask to task:"+str(choice3)+" at position "+str(choice4)+ " has been added successfully.")
                        elif choice4=="":
                            print("Subtasks added successfully.")
                            break
                        else:
                            print("Invalid input.")
            else:
                print("Invalid input")
        elif choice2=="T":
            while True:
                choice3=input("Enter position(number) of your task(Enter only to stop adding)(number of tasks present in current list:"+str(len(ListOfTasks))+"):")
                if choice3.isnumeric():
                    choice3=int(choice3)
                    if choice3==0 or choice3>len(ListOfTasks)+1:
                        print("Sorry we couln't find any such position in list or number is wrong.")
                        continue
                    else:
                        Task=input("Enter the task:")
                        ListOfTasks.insert(choice3-1,[Task])
                        DOC=input("Enter the date of completion:")
                        ListOfTasks[choice3-1].append(DOC)
                        print("Now enter subtasks and enter(only) to stop adding.")
                        cnt=1
                        while True:
                            Subtask=input("Subtask "+str(cnt)+":")
                            cnt+=1
                            if Subtask=="":
                                break
                            else:
                                ListOfTasks[choice3-1].append(Subtask)
                        print("Task at position "+str(choice3)+" has been added successfully.")
                elif choice3=="":
                    print("Tasks added successfully.")
                    break
                else:
                    print("Invalid input.")
        else:
            print("Sorry!, we couldn't get any proper input.")
    elif choice=="R":
        if len(ListOfTasks)!=0:
            choice2=input("Enter your choice to remove a task or subtask or date of complition on existing task list (T/S/D):")
            choice2=choice2.upper()
            if choice2=="T" or choice2=="D":
                choice3=[x for x in input("Enter the number of task(To remove in multiple numbers enter their task number saperated by coma(\",\"))(number of tasks present in current list:"+str(len(ListOfTasks))+"):").split(",")]
                y=True
                for x in range(0,len(choice3)):
                    if not(choice3[x].isnumeric() and (int(choice3[x])!=0 and int(choice3[x])<=len(ListOfTasks))):
                        print("Sorry we couln't find any such task "+str(choice3[x])+" in list or number is wrong.")
                        y=False
                        break
                    elif choice3.count(choice3[x])!=1:
                        print("Task "+str(choice3[x])+" is counted more than one in given input, so this process has been stopped!!!")
                        y=False
                        break
                    else:
                        choice3[x]=int(choice3[x])
                choice3=sorted(choice3)
                if y :
                    for x in range(0,len(choice3)):
                        if choice2=="T":
                            ListOfTasks.pop(choice3[x]-1-x)
                        else:
                            ListOfTasks[choice3[x]-1][1]="No date of complition"
                    if choice2=="T":
                        print("Task no.",choice3," has been removed successfully.")
                    else:
                        print("Date of complition of task no.",choice3," has been removed successfully")
            elif choice2=="S":
                choice3=input("Enter task number and their subtasks numbers saperated bu coma(\",\")(To remove from another task , enter as described and saperatr these by space(\" \"))\n(Example:T1,S1,S2,S3 T2,S4,S5 ...)(number of tasks present in current list:"+str(len(ListOfTasks))+"):")
                choice3=[x for x in choice3.split()]
                y=True
                for x in range(0,len(choice3)):
                    choice3[x]=[x for x in choice3[x].split(",")]
                    if not(choice3[x][0].isnumeric() and (int(choice3[x][0])!=0 and int(choice3[x][0])<=len(ListOfTasks))):
                        print("Sorry we couln't find any such task "+str(choice3[x][0])+" in list or number is wrong.")
                        y=False
                        break
                    elif findtask(choice3,choice3[x][0],x):
                        print("Task "+str(choice3[x][0])+" is counted more than one in given input, so this process has been stopped!!!")
                        y=False
                        break
                    else:
                        choice3[x][0]=int(choice3[x][0])
                        for z in range(1,len(choice3[x])):
                            if not(choice3[x][z].isnumeric() and (int(choice3[x][z])!=0 and int(choice3[x][z])<=len(ListOfTasks[choice3[x][0]-1])-1)):
                                print("Sorry we couln't find any such subtask "+str(choice3[x][y])+" in task "+str(choice3[x][0])+" in list or number is wrong.")
                                y=False
                                break
                            elif choice3[x][1:].count(choice3[x][z]):
                                print("subtask "+str(choice3[x][z])+" in task "+str(choice3[x][0])+" has been counted more than one time so this process has been cancelled succesfully!")
                                y=False
                                break
                            else:
                                choice3[x][z]=int(choice3[x][z])
                        if y==False:
                            break
                if y:
                    choice3=sorted(choice3)
                    l1=[]
                    for x in range(0,len(choice3)):
                        l1=sorted(choice3[x][1:],key=int)
                        for y in range(0,len(l1)):
                            ListOfTasks[choice3[x][0]-1].pop(int(l1[y])+1-y)
                    print("Subtasks removed successfully.")
            else:
                print("Sorry!, we couldn't get any proper input.")
        else:
            print("List is empty.")
    elif choice=="V":
        choice3=input("Do want to see whole list(Enter Y)or a task(Enter task number)(To view multiple tasks enter their number saperated by coma(\",\")(Y/task number):")
        choice3=choice3.upper()
        if len(ListOfTasks)!=0:
            if choice3=="Y":
                for i in range(len(ListOfTasks)):
                    print("\nTask ",i+1,":",ListOfTasks[i][0])
                    print("\tDate of completion :"+str(ListOfTasks[i][1]))
                    for j in range(2,len(ListOfTasks[i])):
                        print("\tSubtask ",j-1,":",ListOfTasks[i][j])
                print()
            elif choice3.isnumeric() and (int(choice3)!=0 and int(choice3)<=len(ListOfTasks)):
                choice3=int(choice3)
                print("\nTask "+str(choice3)+":",ListOfTasks[choice3-1][0])
                print("\tDate of completion :"+str(ListOfTasks[choice3-1][1]))
                for j in range(2,len(ListOfTasks[choice3-1])):
                    print("\tSubtask ",j-1,":",ListOfTasks[choice3-1][j])
            else:
                choice3=[x for x in choice3.split(",")]
                y=True
                for x in range(0,len(choice3)):
                    if not(choice3[x].isnumeric() and (int(choice3[x])!=0 and int(choice3[x])<=len(ListOfTasks))):
                        print("Sorry we couln't find any such task "+str(choice3[x])+" in list or input is wrong.")
                        y=False
                        break
                    elif choice3.count(choice3[x])!=1:
                        print("Task "+str(choice3[x])+" is counted more than one in given input, so this process has been stopped!!!")
                        y=False
                        break
                    else:
                        choice3[x]=int(choice3[x])
                if y :
                    for x in range(0,len(choice3)):
                        print("\nTask "+str(choice3[x])+":",ListOfTasks[choice3[x]-1][0])
                        print("\tDate of completion :"+str(ListOfTasks[choice3[x]-1][1]))
                        for j in range(2,len(ListOfTasks[choice3[x]-1])):
                            print("\tSubtask ",j-1,":",ListOfTasks[choice3[x]-1][j])
        else:
            print("No task to show")
    elif choice=="RE":
        choice2=input("Enter your choice to replace task/subtask/task-subtask or date of complition (T/S/TS/D):")
        choice2=choice2.upper()
        if choice2=="T" or choice2=="D":            
            choice3=input("Enter the first task(number)(number of tasks present in current list:"+str(len(ListOfTasks))+"):")
            if choice3.isnumeric() and (int(choice3)!=0 and int(choice3)<=len(ListOfTasks)):
                choice3=int(choice3)
                choice4=input("Enter the secound task(number)(number of tasks present in current list:"+str(len(ListOfTasks))+")("+str(choice3)+" selected):")
                if choice4.isnumeric() and ((int(choice4)!=0 and int(choice4)<=len(ListOfTasks)) and choice3!=int(choice4)):
                    choice4=int(choice4)
                    if choice2=="T":
                        choice2=input("Do you want to replace whole task(Enter Y) or name only(Enter N) or name and date of completion only(Enter NA)(Y/N/NA):")
                        choice2=choice2.upper()
                        if choice2=="Y":
                            ListOfTasks[choice3-1],ListOfTasks[choice4-1]=ListOfTasks[choice4-1],ListOfTasks[choice3-1]
                            print("Task "+str(choice3)+" and "+str(choice4)+" has been replaced successfully.")
                        elif choice2=="N":
                            ListOfTasks[choice3-1][0],ListOfTasks[choice4-1][0]=ListOfTasks[choice4-1][0],ListOfTasks[choice3-1][0]
                            print("Task "+str(choice3)+" and "+str(choice4)+" has been replaced successfully(names only).")
                        elif choice2=="NA":
                            ListOfTasks[choice3-1][0],ListOfTasks[choice4-1][0]=ListOfTasks[choice4-1][0],ListOfTasks[choice3-1][0]
                            ListOfTasks[choice3-1][1],ListOfTasks[choice4-1][1]=ListOfTasks[choice4-1][1],ListOfTasks[choice3-1][1]
                            print("Task "+str(choice3)+" and "+str(choice4)+" has been replaced successfully(names and date of complition only).")
                    else:
                        ListOfTasks[choice3-1][1],ListOfTasks[choice4-1][1]=ListOfTasks[choice4-1][1],ListOfTasks[choice3-1][1]
                        print("Date of complition of tasks "+str(choice3)+" and "+str(choice4)+" has been replaced successfully.")
                else:
                    print("Invalid input for the secound task(number).")
            else:
                print("Invalid input for the first task(number).")                            
        elif choice2=="S":
            choice,choice2=input("Enter the first subtasks's task(number) and number of subtask saperated by coma(\",\")(Task,Subtask):").split(",")
            if (choice.isnumeric() and (int(choice)!=0 and int(choice)<=len(ListOfTasks))) and (choice2.isnumeric() and (int(choice2)!=0 and int(choice2)<len(ListOfTasks[int(choice)-1])-1)):
                choice=int(choice)
                choice2=int(choice2)
                choice3,choice4=input("Enter the secound subtasks's task(number) and number of subtask saperated by coma(\",\")(Task,Subtask):").split(",")
                if (choice3.isnumeric() and (int(choice3)!=0 and int(choice3)<=len(ListOfTasks))) and (choice4.isnumeric() and (int(choice4)!=0 and int(choice4)<len(ListOfTasks[int(choice3)-1])-1)):
                    choice3=int(choice3)
                    choice4=int(choice4)
                    if choice!=choice3 and choice2!=choice4:
                        ListOfTasks[choice-1][choice2+1],ListOfTasks[choice3-1][choice4+1]=ListOfTasks[choice3-1][choice4+1],ListOfTasks[choice-1][choice2+1]
                        print("Subtask "+str(choice2)+" of task "+str(choice)+" and subtask "+str(choice4)+" of task "+str(choice3)+" replaced successfully.")
                    else:
                        print("Invalid input.")
                else:
                    print("Invalid input.")
            else:
                print("Invalid input.")
            choice="RE"
        elif choice2=="TS":
            choice2=input("Enter the first task(number):")
            if choice2.isnumeric() and (int(choice2)!=0 and int(choice2)<=len(ListOfTasks)):
                choice2=int(choice2)
                choice3,choice4=input("Enter the secound subtasks's task(number) and number of subtask saperated by coma(\",\")(Task,Subtask):").split(",")
                if (choice3.isnumeric() and (int(choice3)!=0 and int(choice3)<=len(ListOfTasks))) and (choice4.isnumeric() and (int(choice4)!=0 and int(choice4)<len(ListOfTasks[int(choice3)-1])-1)):
                    choice3=int(choice3)
                    choice4=int(choice4)
                    ListOfTasks[choice2-1][0],ListOfTasks[choice3-1][choice4+1]=ListOfTasks[choice3-1][choice4+1],ListOfTasks[choice2-1][0]
                    print("Task "+str(choice2)+" and subtask "+str(choice4)+" of task "+str(choice3)+" replaced successfully.")
                else:
                    print("Invalid input.")
            else:
                print("Invalid input.")
        else:
            print("Sorry!, we couldn't get any proper input.")
    elif choice=="S" or choice=="SE":
        data=""
        for x in range(len(ListOfTasks)):
            data+="--task--"+str(ListOfTasks[x][0])
            for y in range(1,len(ListOfTasks[x])):
                data+="--subtask--"+str(ListOfTasks[x][y])
        file=open("task.txt","w")
        file.write(str(data))
        file.close()
        if choice=="SE":
            print("Saved and exited successfully")
            break
        print("Saved successfully!")
    elif choice=="ED":
        choice2=input("Enter your choice to edit a task or subtask or date or completion on existing task (T/S/D):")
        choice2=choice2.upper()
        if choice2=="T" or choice2=="D":
            choice3=input("Enter the number of task(number of tasks present in current list:"+str(len(ListOfTasks))+"):")
            if choice3.isnumeric() and (int(choice3)!=0 and int(choice3)<=len(ListOfTasks)):
                choice3=int(choice3)
                if choice2=="T":
                    print("Previous task:"+str(ListOfTasks[choice3-1][0]))
                    ListOfTasks[choice3-1][0]=input("Enter a new task:")
                    print("Task "+str(choice3)+" has been edited successfully.")
                elif choice2=="D":
                    print("Task's previous date of complition:"+str(ListOfTasks[choice3-1][1]))
                    ListOfTasks[choice3-1][1]=input("Enter a new date of complition:")
                    print("Task "+str(choice3)+"'s date of complition has been edited successfully.")
            else:
                print("Invalid input.")
        elif choice2=="S":
            choice3,choice4=input("Enter the secound subtasks's task(number) and number of subtask saperated by coma(\",\")(Task,Subtasks):").split(",")
            if (choice3.isnumeric() and (int(choice3)!=0 and int(choice3)<=len(ListOfTasks))) and (choice4.isnumeric() and (int(choice4)!=0 and int(choice4)<len(ListOfTasks[int(choice3)-1])-1)):
                choice3=int(choice3)
                choice4=int(choice4)
                print("Previous subtask:"+str(ListOfTasks[choice3-1][choice4+1]))
                ListOfTasks[choice3-1][choice4+1]=input("Enter a new subtask:")
                print("Subtask "+str(choice4)+" of task "+str(choice3)+ " has been edited successfully.")                
            else:
                print("Invalid input.")
        else:
            print("Sorry!, we couldn't get any proper input.")
    elif choice=="D":
        if len(ListOfTasks)!=0:
            choice2=input("Are you sure want to delete whole list and make empty list (Y/N):")
            choice2=choice2.upper()
            if choice2=="Y" :
                file=open("task.txt","w")
                file.close()
                ListOfTasks=[]
                print("List has been deleted successfully.")
            else:
                print("Deleting process has been cancelled successfully")
        else:
            print("List is already empty.")
    else:
        print("Sorry, we couldn't get any proper input.")
