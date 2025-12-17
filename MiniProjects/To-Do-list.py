tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

while True:
    choice = input("Add/Show/Remove/Quit: ").lower()
    if choice == "add":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "show":
        show_tasks()
    elif choice == "remove":
        show_tasks()
        index = int(input("Enter task number to remove: ")) - 1
        remove_task(index)
    elif choice == "quit":
        break
