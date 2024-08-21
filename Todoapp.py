tasks = []
def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def listTasks():
    if not tasks:
        print("There are no task currently")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {tasks}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter # to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)

            print(f"task {taskToDelete} has been removed.")
        else:
            print(f"Task # {taskToDelete} was not found.")
    except:
        print("Invalid Input.")

if __name__== "__main__":
    #create a loop to run the app
    print("welcome to the to do list app")
    while True:
        print("\n")
        print("please select one of the following options")
        print("------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List task")
        print("4. Quit")

    choice = input("Enter your choice: ")

    if(choice == "1"):
        addTask()
    elif(choice == "2"):
        deleteTask()
    elif(choice == "3"):
        listTask()

    elif(choice == "4"):
        'break'
    else:
        print("Invalid input. Please try again.")
        print("Goodbye👋👋")


first_task= input(("1.Enter the next task please: "))
second_task= input(("2.Enter the next task please: "))
third_task= input(("3.Enter the next task please: "))
fourth_task= input(("4.Enter the next task please: "))
fifth_task= input(("5.Enter the next text please: "))
print(f"task for today is: 1.{first_task} 2.{second_task} 3.{third_task} 4.{fourth_task} 5.{fifth_task}")