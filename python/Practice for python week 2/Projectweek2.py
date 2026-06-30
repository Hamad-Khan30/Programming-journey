tasks = []
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    Task = input("Enter your task: ")
    if Task == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task add sucessfully")

    elif Task == "2":
        if len(tasks) == 0:
            print("No task found ")
        else:
            print("\nTasks: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif Task == "3":
        if len(tasks) == 0:
            print("No task for delete ")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted ")
            else:
                print("invalid number ")

    elif Task == "4":
        print("okyy")
        break

    else:
        print("invalid Task")