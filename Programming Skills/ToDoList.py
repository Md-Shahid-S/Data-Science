# Creating simple ToDo list using Python

def todo():
    tasks = []
    
    print("\n1. Add a Task \n2. View the task \n3. Remove  a task \n4. Exit")
    

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            tasks.append(input("Enter your Task:"))
        elif choice == '2':
            if tasks:
               for i, task in enumerate(tasks):
                    print("{}. {}".format(i+1, task))
            else:
                print("No tasks to show")
        elif choice == '3':
            if tasks:
                num = int(input("Enter the task number to remove: "))
                if 0 <= num >= len(tasks):
                    tasks.pop(num-1)
                else:
                    print("Invalid Task number")
            else:
                print("No tasks to remove")
        elif choice == '4':
            break

todo()
