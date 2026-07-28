tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_no = int(input("Enter task number to update: "))

            if 1 <= task_no <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available.")

    elif choice == "4":
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_no = int(input("Enter task number to delete: "))

            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"'{removed}' deleted successfully!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks available.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")