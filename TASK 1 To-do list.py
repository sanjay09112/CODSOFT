tasks = []
completed = []

def add():
    global tasks
    n = int(input("Enter how many tasks to add: "))
    for i in range(n):
        task = input(f"Enter task {i+1}: ")
        tasks.append(task)
        completed.append(False)

def include():
    task = input("Enter the new task to add: ")
    tasks.append(task)
    completed.append(False)

def view():
    if tasks:
        for idx, task in enumerate(tasks):
            status = "completed" if completed[idx] else "not completed yet"
            print(f"Task {idx+1}: {task} - {status}")
    else:
        print("Nothing stored in task list")

def remove():
    if tasks:
        num = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
            completed.pop(num)
        else:
            print("Invalid task number")
    else:
        print("Nothing stored in task list")

def mark():
    if tasks:
        num = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= num < len(tasks):
            completed[num] = True
        else:
            print("Invalid task number")
    else:
        print("Nothing stored in task list")


run = True
while run:
    print("\nTo perform a task, enter the corresponding task number:")
    print("1. To add task enter 1")
    print("2. To view tasks enter 2")
    print("3. To remove task enter 3")
    print("4. To mark task as completed enter 4")
    print("5. To add task to the existing tasks enter 5")
    print("6. To end the process enter 6\n")
    option = int(input("Enter your choice: "))
    if option == 1:
        add()
    elif option == 2:
        view()
    elif option == 3:
        remove()
    elif option == 4:
        mark()
    elif option == 5:
        include()
    elif option == 6:
        run = False
    else:
        print("INVALID OPTION")