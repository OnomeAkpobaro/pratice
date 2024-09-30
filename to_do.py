def todo_list():
    tasks = []
    while True:
        print("\nMenu: 1. Add Task 2. Remove Task 3. View Task 4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            print("Task Added")
            task = input("Enter Task: ")
            tasks.append(task)
                
        elif choice == '2':
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found")
        elif choice == '3':
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '4':
            print("Exiting..")
            break
        else:
            print("Invalid choice")
todo_list()
