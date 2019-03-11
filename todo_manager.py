tasks=[]
while(1):
    print("Insert the number corresponding to the action you want to perform:")
    print("1. insert a new task;")
    print("2. remove a task;")
    print("3. show all the tasks;")
    print("4. close the program.")
    choice=int(input("Your choice: "))
    if(choice==1):
        tasks.append(input("Insert a new task: "))
    elif(choice==2):
        for task in tasks:
            print(task)
        tasks.remove(input())
        index=0
    elif(choice==3):
        for var in tasks:
            print(var, "")
    elif( choice==4 ):
        break
    else:
        print("Retry your choice")
