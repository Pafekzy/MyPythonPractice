tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)

def view_tasks():
    print("To-Do List:")
    for task in tasks:
        print(f"- {task}")

while True:
    command = input("Enter a command (add, remove, view, exit): ").strip().lower()
    if command == 'add':
        task = input("Enter a task: ")
        add_task(task)
    elif command == 'remove':
        task = input("Enter a task to remove: ")
        remove_task(task)
    elif command == 'view':
        view_tasks()
    elif command == 'exit':
        break
    else:
        print("Unknown command")


commandlinetodolist
