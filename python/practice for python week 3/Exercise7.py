class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
    
    def mark_complete(self):
        self.done = True
    
    def mark_incomplete(self):
        self.done = False
    
    def __str__(self):
        return f"{self.description}"

class TodoList:
    def __init__(self, name="My Tasks"):
        self.name = name
        self.tasks = []
    
    def add(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added: '{description}'")
        return task
    
    def complete(self, index):
        try:
            self.tasks[index-1].mark_complete()
            print(f"Completed: '{self.tasks[index-1].description}'")
        except IndexError:
            print(f"Task #{index} not found!")
    
    def incomplete(self, index):
        try:
            self.tasks[index-1].mark_incomplete()
            print(f"Reopened: '{self.tasks[index-1].description}'")
        except IndexError:
            print(f"Task #{index} not found!")
    
    def delete(self, index):
        try:
            task = self.tasks.pop(index-1)
            print(f"Deleted: '{task.description}'")
        except IndexError:
            print(f"Task #{index} not found!")
    
    def show(self):
        if not self.tasks:
            print(f"\n{self.name} is empty!\n")
            return
        print(f"\n{self.name}:")
        print("-"*50)
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task.done else "Pending"
            print(f"  {i}. {task} - {status}")
        print("-"*50)
        completed = sum(1 for t in self.tasks if t.done)
        print(f"  Total: {len(self.tasks)} | Done: {completed} | Pending: {len(self.tasks)-completed}\n")
    
    def show_pending(self):
        pending = [t for t in self.tasks if not t.done]
        if not pending:
            print("\nAll done!\n")
            return
        print(f"\n{self.name} (Pending):")
        print("-"*50)
        for i, task in enumerate(pending, 1):
            print(f"  {i}. {task}")
        print("-"*50)
        print(f"  Pending: {len(pending)}\n")
    
    def clear_done(self):
        done = [t for t in self.tasks if t.done]
        if not done:
            print("No completed tasks!")
            return
        self.tasks = [t for t in self.tasks if not t.done]
        print(f"Cleared {len(done)} tasks!")
    
    def search(self, keyword):
        found = [t for t in self.tasks if keyword.lower() in t.description.lower()]
        if found:
            print(f"\nFound {len(found)} task(s):")
            for i, task in enumerate(found, 1):
                print(f"  {i}. {task}")
            print()
        else:
            print(f"No tasks found for '{keyword}'\n")
        return found
    
    def __str__(self):
        done = sum(1 for t in self.tasks if t.done)
        return f"{self.name}: {len(self.tasks)} total, {done} done, {len(self.tasks)-done} pending"

todo = TodoList()
todo.add("Learn Python")
todo.add("Build app")
todo.add("Read book")
todo.show()
todo.complete(1)
todo.complete(3)
todo.show()
todo.show_pending()
todo.search("python")
todo.delete(2)
todo.show()
todo.clear_done()
todo.show()