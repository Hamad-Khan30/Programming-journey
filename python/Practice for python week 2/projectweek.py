tasks=[]
def add_task():
    Task=input("Please write your task: ")
    tasks.append(Task)
    print("Your task added sucessfully")

def view_task():
    if len(tasks)==0:
        print("There is no task, so first enetr your task")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i} : {task}")

def delete_task():
    if len(tasks)==0:
        print("There is no task")
    else:
        view_task()
        num=input("Enter the task number you want to delete: ")

        if not num.isdigit():
            print("Please enter number in digits ")
            return

    num = int(num)

    if num <= len(tasks) and num >= 1:
        tasks.pop(num-1)
        print("Task deleted Sucessfully")
    else:
        print("Your no. is not valid")

while True:
    print("1. Add task")
    print("2. View task")
    print("3. Delete task")
    print("4. Quit")

    choice=input("Please enter your task: ")

    if not choice.isdigit():
        print("Please enter a valid number between 1 and 4")
        continue

    choice = int(choice)

    

    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        delete_task()
    elif choice==4:
        print("You sucessfully quite from this site")
    else:
        print("Your task no. is invalid")
 
