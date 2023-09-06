tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Your task {task} is added to the to do list")
    
def remove_task(index):
    if index >= 1 and index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' has been removed from the to-do list.")
    else:
        print("Invalid task index.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            index_to_remove = int(input("Enter the index of the task to remove: "))
            remove_task(index_to_remove)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
