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
        num=int(input("Enter the task number you want to delete: "))
        if num < len(tasks) and num > 1:
            tasks.pop(num-1)
            print("Task deleted Sucessfully")
        else:
            print("Your no. is not valid")